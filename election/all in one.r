# the mother script that calls all the others
library(data.table)
library(lubridate)
library(ggplot2)
library(ggthemes)


#######################
#
# DOWNLOAD THE DATA
#
#######################
download.file("https://projects.fivethirtyeight.com/polls/data/president_polls.csv", 
              destfile = basename("presidential_polls_for_use.csv"))
data <- fread("presidential_polls_for_use.csv")


######################
#
# PROCESS THE DATA
#
#####################
length(unique(data$poll_id))


candidate_data <- dcast(data, poll_id+sample_size+population+end_date+state~answer, mean, value.var = "pct")
candidate_data[is.na(candidate_data)] <- 0

bt_data <- candidate_data[candidate_data$Biden > 0]
bt_data <- bt_data[bt_data$Trump > 0]
bt_data <- bt_data[,c("poll_id", "end_date", "sample_size", "population", "state",
                      "Biden", "Trump", "DeSantis", "Harris", "Kennedy", "West", 
                      "Haley", "Mapstead", "Manchin", "Newsom", "Pence", "Scott",
                      "Ramaswamy", "Cheney", "Christie", "Clinton", "Whitmer", 
                      "Sanders")]
bt_data
bt_data <- bt_data[bt_data$sample_size > 0]
# bt_data <- bt_data[bt_data$DeSantis == 0]
# bt_data <- bt_data[bt_data$Harris == 0]
# bt_data <- bt_data[bt_data$Kennedy == 0]
# bt_data <- bt_data[bt_data$West == 0]
# bt_data <- bt_data[bt_data$Haley == 0]
# bt_data <- bt_data[bt_data$Mapstead == 0]
# bt_data <- bt_data[bt_data$Manchin == 0]
# bt_data <- bt_data[bt_data$Newsom == 0]
# bt_data <- bt_data[bt_data$Pence == 0]
# bt_data <- bt_data[bt_data$Scott == 0]
# bt_data <- bt_data[bt_data$Ramaswamy == 0]
# bt_data <- bt_data[bt_data$Cheney == 0]
# bt_data <- bt_data[bt_data$Christie == 0]
# bt_data <- bt_data[bt_data$Clinton == 0]
# bt_data <- bt_data[bt_data$Whitmer == 0]
# bt_data <- bt_data[bt_data$Sanders == 0]

bt_data$BT_total <- bt_data$Biden + bt_data$Trump
bt_data <- bt_data[,c("poll_id", "end_date", "sample_size", "population", "state",
                      "Biden", "Trump")]
bt_data
bt_data <- bt_data[bt_data$population != "v"]
bt_data$population_weight <- ifelse(bt_data$population == "a", 0.628, bt_data$population)
bt_data$population_weight <- ifelse(bt_data$population == "rv", 0.753, bt_data$population_weight)
bt_data$population_weight <- ifelse(bt_data$population == "lv", 1, bt_data$population_weight)
bt_data$population_weight <- as.numeric(bt_data$population_weight)

bt_data$end_date <- mdy(bt_data$end_date)
bt_data$date_weight <- 0.5**as.numeric((Sys.Date()-bt_data$end_date)/14)
bt_data$sample_weight <- 1+log10(bt_data$sample_size/1000)
bt_data$Biden_Win <- ifelse(bt_data$Biden >= bt_data$Trump, 1, 0)
bt_data$Trump_win <- ifelse(bt_data$Biden < bt_data$Trump, 1, 0)


bt <- bt_data
bt

bt$wbw <- bt$Biden_Win
bt$wbw <- bt$wbw * bt$population_weight * bt$sample_weight * bt$date_weight
bt$wtw <- bt$Trump_win
bt$wtw <- bt$wtw * bt$population_weight * bt$sample_weight * bt$date_weight
bt

pv <- bt[bt$state == ""]

fwrite(pv, file="popular_vote_polls.csv")
pv$wtw
sum(pv$wtw)
sum(pv$wbw)

state_wbw <- dcast(bt, state~., sum, value.var="wbw")
state_wtw <- dcast(bt, state~., sum, value.var="wtw")

colnames(state_wbw) <- c("state", "wbw")
colnames(state_wtw) <- c("state", "wtw")

states <- merge(state_wbw, state_wtw)
states <- states[states$state %in% c("Arizona", "Georgia", "Florida", "Michigan", "Nevada", "North Carolina", "Pennsylvania", "Wisconsin")]

states$wbw <- round(states$wbw, digits=2)
states$wtw <- round(states$wtw, digits=2)
states

fwrite(states, file="states.csv")

pv_export <- data.table(cand = c("Biden", "Trump"), wins=c(sum(pv$wbw), sum(pv$wtw)))
pv_export
fwrite(pv_export, "pv_export.csv")



######################
#
# POPULAR VOTE
#
######################

data <- data.table(p=c(0:20)/20)
pv <- fread("pv_export.csv")
w = as.numeric(pv[1,2])	
l = as.numeric(pv[2,2])


date <- Sys.Date()


data$density <- data$p**w*(1-data$p)**l# * factorial(w+l+1)/(factorial(w)*factorial(l))
data$density <- data$density / sum(data$density)
data$category <- fifelse(data$p < 0.5, "Trump Win More Likely", "Biden Win More Likely")
data$category <- as.character(data$category)

# max value
# data[order(-ways)][1,1]

# plotting
ggplot(data, aes(x=as.integer(p*100), y=density))+
  geom_col(aes(fill=category), size=1.5)+
  scale_fill_manual(values=c(
    "Trump Win More Likely"="#ee4444",
    "Biden Win More Likely"="#0077ee"
  ))+
  #geom_vline(xintercept = as.numeric(data[order(-density)][1,1]), linetype="dotted", color="#666666", size=1)+
  geom_vline(xintercept = 50, color="#000000", size=1, linetype="dotted")+
  theme_bw()+
  xlab("Probability that Biden Wins Popular Vote")+
  ylab("Relative Density of that Probability being true")+
  theme(legend.position = "bottom")+
  scale_x_continuous(breaks=seq(0,100,5),expand = c(0,0), limits=c(0,101))+
  scale_y_continuous(expand=c(0,0), limits=c(0,0.4))+
  theme(axis.line = element_line(color='black'),
        plot.background = element_blank(),
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        panel.border = element_blank())+
  labs(title="Popular Vote", subtitles=paste("Prediction as of:",date))

ggsave(paste0("popular vote ", date, ".png"))



#########################
#
# STATES
#
#########################

state_plots <- function(state, date, data, w, l){
  
  data$density <- data$p**w*(1-data$p)**l# * factorial(w+l+1)/(factorial(w)*factorial(l))
  data$density <- data$density / sum(data$density)
  data$category <- fifelse(data$p < 0.5, "Trump Win More Likely", "Biden Win More Likely")
  data$category <- as.character(data$category)
  
  # max value
  # data[order(-ways)][1,1]
  
  
  # plotting
  g <- ggplot(data, aes(x=as.integer(p*100), y=density))+
    geom_col(aes(fill=category), size=1.5)+
    scale_fill_manual(values=c(
      "Trump Win More Likely"="#ee4444",
      "Biden Win More Likely"="#0077ee"
    ))+
    #geom_vline(xintercept = as.numeric(data[order(-density)][1,1]), linetype="dotted", color="#666666", size=1)+
    geom_vline(xintercept = 50, color="#000000", size=1, linetype="dotted")+
    theme_bw()+
    xlab("Probability that Biden Wins Popular Vote")+
    ylab("Relative Density of that Probability being true")+
    theme(legend.position = "bottom")+
    scale_x_continuous(breaks=seq(0,100,5),expand = c(0,0), limits=c(0,101))+
    scale_y_continuous(expand=c(0,0), limits=c(0,0.25))+
    theme(axis.line = element_line(color='black'),
          plot.background = element_blank(),
          panel.grid.major = element_blank(),
          panel.grid.minor = element_blank(),
          panel.border = element_blank())+
    labs(title=state, subtitles=date)
  #ggsave(filename = paste(state, date,'png'), g)
  g
}

date <- Sys.Date()

data <- data.table(p=c(0:20)/20)

sd <- fread("states.csv")

state_plots(       "Arizona", date, data, as.numeric(sd[1,2]), as.numeric(sd[1,3]))
ggsave(paste("Arizona", date, ".png"))

state_plots(       "Georgia", date, data, as.numeric(sd[3,2]), as.numeric(sd[1,3]))
ggsave(paste("Georgia", date, ".png"))

state_plots(       "Florida", date, data, as.numeric(sd[2,2]), as.numeric(sd[2,3]))
ggsave(paste("Florida", date, ".png"))

state_plots(     "Michigan", date, data, as.numeric(sd[4,2]), as.numeric(sd[4,3]))
ggsave(paste("Michigan", date, ".png"))

state_plots(        "Nevada", date, data, as.numeric(sd[5,2]), as.numeric(sd[5,3]))
ggsave(paste("Nevada", date, ".png"))

state_plots("North Carolina", date, data, as.numeric(sd[6,2]), as.numeric(sd[6,3]))
ggsave(paste("North Carolina", date, ".png"))

state_plots(  "Pennsylvania", date, data, as.numeric(sd[7,2]), as.numeric(sd[7,3]))
ggsave(paste("Pennsylvania", date, ".png"))

state_plots(     "Wisconsin", date, data, as.numeric(sd[8,2]), as.numeric(sd[8,3]))
ggsave(paste("Wisconsin", date, ".png"))



######################
#
# BINOMIAL PLOT
#
######################

data <- fread("popular_vote_polls.csv")



# set up the variables
n <- data$sample_size[1]
x <- as.integer(data$sample_size * data$Biden/100)[1]
probabilities <- seq(0, 0.99, by = 0.01)

# Calculate binomial probabilities
binom_probabilities <- dbinom(600, size = 1000, prob = probabilities)

# Display the result
binom_probabilities

# Create a data frame with probabilities as column names
result_table <- data.table((rbind(as.character(probabilities), binom_probabilities)))
setnames(result_table, as.character(result_table[1, ]))
result_table <- result_table[-1, ]
output_table <- result_table

for (i in c(2:nrow(data))) {
  # set up the variables
  n <- data$sample_size[i]
  x <- as.integer(data$sample_size * data$Biden/100)[i]
  probabilities <- seq(0, 0.99, by = 0.01)
  
  # Calculate binomial probabilities
  binom_probabilities <- dbinom(x, size = n, prob = probabilities)
  
  # Create a data frame with probabilities as column names
  result_table <- data.table((rbind(as.character(probabilities), binom_probabilities)))
  setnames(result_table, as.character(result_table[1, ]))
  result_table <- result_table[-1, ]
  
  output_table <- rbind(output_table, result_table)
}

output_table[, names(output_table) := lapply(.SD, as.numeric)]

d <- data.table(colsums = colSums(output_table))
d$vote_share <- colnames(output_table)
d

biden_plot <- ggplot(d, aes(y=colsums/sum(colsums), x=as.numeric(vote_share)))+
  geom_col(alpha=0.5, fill="blue")+
  theme_bw()





# set up the variables
n <- data$sample_size[1]
x <- as.integer(data$sample_size * data$Trump/100)[1]
probabilities <- seq(0, 0.99, by = 0.01)

# Calculate binomial probabilities
binom_probabilities <- dbinom(600, size = 1000, prob = probabilities)

# Display the result
binom_probabilities

# Create a data frame with probabilities as column names
result_table <- data.table((rbind(as.character(probabilities), binom_probabilities)))
setnames(result_table, as.character(result_table[1, ]))
result_table <- result_table[-1, ]
trump_output_table <- result_table

for (i in c(2:nrow(data))) {
  # set up the variables
  n <- data$sample_size[i]
  x <- as.integer(data$sample_size * data$Trump/100)[i]
  probabilities <- seq(0, 0.99, by = 0.01)
  
  # Calculate binomial probabilities
  binom_probabilities <- dbinom(x, size = n, prob = probabilities)
  
  # Create a data frame with probabilities as column names
  result_table <- data.table((rbind(as.character(probabilities), binom_probabilities)))
  setnames(result_table, as.character(result_table[1, ]))
  result_table <- result_table[-1, ]
  
  trump_output_table <- rbind(trump_output_table, result_table)
}

trump_output_table[, names(trump_output_table) := lapply(.SD, as.numeric)]

trump_d <- data.table(colsums = colSums(trump_output_table))
trump_d$vote_share <- colnames(trump_output_table)
trump_d

colnames(d) <- c("Biden", "Vote Share")
colnames(trump_d) <- c("Trump", "Vote Share")

#get the max for biden
bmax <- d[order(-Biden)]
tmax <- trump_d[order(-Trump)]

ggplot()+
  scale_x_continuous(breaks = seq(0, 100, by = 10))+
  geom_area(data=d, aes(x=as.numeric(`Vote Share`)*100, y=Biden), fill="#0077ee", alpha=0.9)+
  geom_area(data=trump_d, aes(x=as.numeric(`Vote Share`)*100, y=Trump), fill="#ee4444", alpha=0.9)+
  geom_vline(xintercept = as.numeric(bmax[1,2])*100, color="#0000aa", alpha=0.9)+
  geom_vline(xintercept = as.numeric(tmax[1,2])*100, color="#aa0000", alpha=0.9)+
  xlab("Percentage of Vote")+
  ylab("Relative Likelihood")+
  labs(title="Relative Likelihood of Biden and Trump Vote Share in Popular Vote",
       subtitle="Biden is in Blue, Trump is in Red, vertical lines indicate the highest probability")+
  theme_bw()

ggsave(filename = paste(Sys.Date(),"binomial plot.png"))



#########################
#
# ELECTORAL COLLEGE
#
#########################

library(ggdist)

data <- data.table(Trump = c(199, 208, 218, 205, 215, 224, 234, 195, 205, 214, 224, 211, 221, 230, 240, 199, 209, 218, 228, 215, 225, 234, 244, 205, 215, 224, 234, 221, 231, 240, 250, 219, 229, 238, 248, 235, 245, 254, 264, 225, 235, 244, 254, 241, 251, 260, 270, 229, 239, 248, 258, 245, 255, 264, 274, 235, 245, 254, 264, 251, 261, 270, 280, 205, 215, 224, 234, 221, 231, 240, 250, 211, 221, 230, 240, 227, 237, 246, 256, 215, 225, 234, 244, 231, 241, 250, 260, 221, 231, 240, 250, 237, 247, 256, 266, 235, 245, 254, 264, 251, 261, 270, 280, 241, 251, 260, 270, 257, 267, 276, 286, 245, 255, 264, 274, 261, 271, 280, 290, 251, 261, 270, 280, 267, 277, 286, 296, 210, 219, 229, 216, 226, 235, 245, 206, 216, 225, 235, 222, 232, 241, 251, 210, 220, 229, 239, 226, 236, 245, 255, 216, 226, 235, 245, 232, 242, 251, 261, 230, 240, 249, 259, 246, 256, 265, 275, 236, 246, 255, 265, 252, 262, 271, 281, 240, 250, 259, 269, 256, 266, 275, 285, 246, 256, 265, 275, 262, 272, 281, 291, 216, 226, 235, 245, 232, 242, 251, 261, 222, 232, 241, 251, 238, 248, 257, 267, 226, 236, 245, 255, 242, 252, 261, 271, 232, 242, 251, 261, 248, 258, 267, 277, 246, 256, 265, 275, 262, 272, 281, 291, 252, 262, 271, 281, 268, 278, 287, 297, 256, 266, 275, 285, 272, 282, 291, 301, 262, 272, 281, 291, 278, 288, 297, 307))
data$Biden <- 538 - data$Trump
data$category <- fifelse(data$Biden > 270, "Biden Win", "Trump Win")
data$Likelihood <- c(6.20648E-08, 3.35588E-07, 2.06954E-07, 2.09904E-06, 1.29446E-06, 6.99923E-06, 4.31638E-06, 1.50962E-06, 9.30972E-07, 5.03381E-06, 3.10432E-06, 3.14856E-05, 1.94169E-05, 0.000104988, 6.47456E-05, 1.16774E-07, 7.20134E-08, 3.8938E-07, 2.40128E-07, 2.4355E-06, 1.50196E-06, 8.12117E-06, 5.00827E-06, 1.7516E-06, 1.0802E-06, 5.8407E-06, 3.60192E-06, 3.65326E-05, 2.25294E-05, 0.000121818, 7.5124E-05, 8.56826E-07, 5.28398E-07, 2.85708E-06, 1.76194E-06, 1.78705E-05, 1.10206E-05, 5.9589E-05, 3.67481E-05, 1.28524E-05, 7.92597E-06, 4.28562E-05, 2.64291E-05, 0.000268058, 0.000165309, 0.000893836, 0.000551222, 9.9417E-07, 6.13097E-07, 3.31505E-06, 2.04437E-06, 2.0735E-05, 1.27872E-05, 6.91408E-05, 4.26387E-05, 1.49125E-05, 9.19646E-06, 4.97258E-05, 3.06655E-05, 0.000311026, 0.000191807, 0.001037112, 0.00063958, 8.17822E-07, 5.04345E-07, 2.72702E-06, 1.68173E-06, 1.7057E-05, 1.05189E-05, 5.68765E-05, 3.50753E-05, 1.22673E-05, 7.56518E-06, 4.09053E-05, 2.5226E-05, 0.000255855, 0.000157784, 0.000853148, 0.00052613, 9.48915E-07, 5.85189E-07, 3.16415E-06, 1.95131E-06, 1.97912E-05, 1.22051E-05, 6.59935E-05, 4.06977E-05, 1.42337E-05, 8.77783E-06, 4.74622E-05, 2.92696E-05, 0.000296868, 0.000183076, 0.000989902, 0.000610466, 6.96266E-06, 4.29382E-06, 2.32169E-05, 1.43177E-05, 0.000145218, 8.95547E-05, 0.000484227, 0.000298619, 0.00010444, 6.44073E-05, 0.000348254, 0.000214766, 0.002178265, 0.001343321, 0.007263407, 0.004479291, 8.07873E-06, 4.9821E-06, 2.69385E-05, 1.66128E-05, 0.000168495, 0.00010391, 0.000561846, 0.000346486, 0.000121181, 7.47314E-05, 0.000404077, 0.000249191, 0.002527429, 0.001558647, 0.00842769, 0.005197296, 1.27963E-06, 6.91903E-06, 4.26691E-06, 4.32773E-05, 2.66888E-05, 0.000144308, 8.89935E-05, 3.11248E-05, 1.91944E-05, 0.000103785, 6.40037E-05, 0.000649159, 0.000400332, 0.002164615, 0.001334903, 2.4076E-06, 1.48475E-06, 8.02811E-06, 4.95088E-06, 5.02144E-05, 3.09668E-05, 0.000167439, 0.000103259, 3.61139E-05, 2.22712E-05, 0.000120422, 7.42632E-05, 0.000753216, 0.000464503, 0.002511591, 0.00154888, 1.76657E-05, 1.08943E-05, 5.89062E-05, 3.6327E-05, 0.000368448, 0.000227219, 0.001228586, 0.00075766, 0.000264986, 0.000163415, 0.000883593, 0.000544906, 0.005526718, 0.003408287, 0.018428794, 0.011364905, 2.04974E-05, 1.26406E-05, 6.83486E-05, 4.21501E-05, 0.000427508, 0.000263641, 0.001425522, 0.000879109, 0.000307462, 0.000189609, 0.001025228, 0.000632251, 0.00641262, 0.003954616, 0.021382824, 0.013186634, 1.68616E-05, 1.03984E-05, 5.62248E-05, 3.46734E-05, 0.000351676, 0.000216876, 0.00117266, 0.000723171, 0.000252924, 0.000155976, 0.000843372, 0.000520101, 0.005275139, 0.00325314, 0.017589903, 0.010847567, 1.95644E-05, 1.20652E-05, 6.52373E-05, 4.02314E-05, 0.000408048, 0.00025164, 0.001360631, 0.000839091, 0.000293466, 0.000180978, 0.000978559, 0.000603471, 0.006120713, 0.0037746, 0.020409464, 0.01258637, 0.000143554, 8.85285E-05, 0.000478678, 0.000295198, 0.002994048, 0.001846408, 0.009983627, 0.006156831, 0.002153305, 0.001327928, 0.007180177, 0.004427964, 0.04491072, 0.027696118, 0.1497544, 0.092352461, 0.000166565, 0.000102719, 0.000555408, 0.000342516, 0.003473977, 0.002142377, 0.011583945, 0.007143736, 0.002498468, 0.001540787, 0.008331119, 0.005137741, 0.052109652, 0.032135648, 0.173759176, 0.107156034)


dt <- dcast(data, Biden~., sum, value.var = "Likelihood")
colnames(dt) <- c("Biden Electoral Votes", "Relative Likelihood")
dt$`Relative Likelihood` <- dt$`Relative Likelihood`
dt$category <- fifelse(dt$`Biden Electoral Votes` > 270, "Biden Win", "Trump Win")

ggplot(dt, aes(x=`Biden Electoral Votes`, y=`Relative Likelihood`, fill=category))+
  geom_col()+
  scale_fill_manual(values=c(
    "Trump Win"="#ee4444",
    "Biden Win"="#0077ee"
  ))+
  #geom_vline(xintercept = as.numeric(data[order(-density)][1,1]), linetype="dotted", color="#666666", size=1)+
  theme_bw()+
  theme(legend.position = "bottom")+
  scale_x_continuous(breaks=seq(0,400,5),expand = c(0,0), limits=c(min(dt$`Biden Electoral Votes`),max(dt$`Biden Electoral Votes`)))+
  scale_y_continuous(expand=c(0,0), limits=c(0,0.25))+
  theme(axis.line = element_line(color='black'),
        plot.background = element_blank(),
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        panel.border = element_blank())

date <- Sys.Date()
ggsave(paste0("electoral college ", date, ".png"))
