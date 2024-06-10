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
library(data.table)
library(ggplot2)

data <- fread("popular_vote_polls.csv")



# set up the variables
n <- data$sample_size[1]
x <- as.integer(data$sample_size * data$Biden/(data$Biden + data$Trump))[1]
probabilities <- seq(0.3, 0.7, by = 0.002)

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
  if (i%%10 == 0) {
    print(paste(i, "/", nrow(data)))
  }
  # set up the variables
  n <- data$sample_size[i]
  x <- as.integer(data$sample_size * data$Biden/(data$Biden + data$Trump))[i]
  probabilities <- seq(0.3, 0.7, by = 0.002)
  
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




# set up the variables
n <- data$sample_size[1]
x <- as.integer(data$sample_size * data$Trump/(data$Biden + data$Trump))[1]
probabilities <- seq(0.3, 0.7, by = 0.002)

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
  if (i%%10 == 0) {
    print(paste(i, "/", nrow(data)))
  }
  # set up the variables
  n <- data$sample_size[i]
  x <- as.integer(data$sample_size * data$Trump/(data$Biden + data$Trump))[i]
  probabilities <- seq(0.3, 0.7, by = 0.002)
  
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
  geom_area(data=d, aes(x=as.numeric(`Vote Share`)*100, y=Biden), fill="#0077ee", alpha=0.8)+
  geom_area(data=trump_d, aes(x=as.numeric(`Vote Share`)*100, y=Trump), fill="#ee4444", alpha=0.8)+
  geom_vline(xintercept = as.numeric(bmax[1,2])*100, color="#0000bb", alpha=0.9, linewidth = 0.9)+
  geom_vline(xintercept = as.numeric(tmax[1,2])*100, color="#990000", alpha=0.9, linewidth = 0.9)+
  xlab("Percentage of Vote")+
  ylab("Relative Likelihood")+
  labs(title="Relative Likelihood of Biden and Trump Vote Share in Popular Vote",
       subtitle="Biden is in Blue, Trump is in Red, vertical lines indicate the highest probability")+
  theme_bw()+
  xlim(c(30,70))+
  ylim(c(0,20))

ggsave(filename = paste(Sys.Date(),"binomial plot.png"))


#########################
#
# ELECTORAL COLLEGE
#
#########################
library(data.table)
library(ggplot2)
library(ggdist)
library(fitODBOD)

data <- data.table(Trump = c(199, 208, 218, 205, 215, 224, 234, 195, 205, 214, 224, 211, 221, 230, 240, 199, 209, 218, 228, 215, 225, 234, 244, 205, 215, 224, 234, 221, 231, 240, 250, 219, 229, 238, 248, 235, 245, 254, 264, 225, 235, 244, 254, 241, 251, 260, 270, 229, 239, 248, 258, 245, 255, 264, 274, 235, 245, 254, 264, 251, 261, 270, 280, 205, 215, 224, 234, 221, 231, 240, 250, 211, 221, 230, 240, 227, 237, 246, 256, 215, 225, 234, 244, 231, 241, 250, 260, 221, 231, 240, 250, 237, 247, 256, 266, 235, 245, 254, 264, 251, 261, 270, 280, 241, 251, 260, 270, 257, 267, 276, 286, 245, 255, 264, 274, 261, 271, 280, 290, 251, 261, 270, 280, 267, 277, 286, 296, 210, 219, 229, 216, 226, 235, 245, 206, 216, 225, 235, 222, 232, 241, 251, 210, 220, 229, 239, 226, 236, 245, 255, 216, 226, 235, 245, 232, 242, 251, 261, 230, 240, 249, 259, 246, 256, 265, 275, 236, 246, 255, 265, 252, 262, 271, 281, 240, 250, 259, 269, 256, 266, 275, 285, 246, 256, 265, 275, 262, 272, 281, 291, 216, 226, 235, 245, 232, 242, 251, 261, 222, 232, 241, 251, 238, 248, 257, 267, 226, 236, 245, 255, 242, 252, 261, 271, 232, 242, 251, 261, 248, 258, 267, 277, 246, 256, 265, 275, 262, 272, 281, 291, 252, 262, 271, 281, 268, 278, 287, 297, 256, 266, 275, 285, 272, 282, 291, 301, 262, 272, 281, 291, 278, 288, 297, 307))
data$Biden <- 538 - data$Trump
data$category <- fifelse(data$Biden > 270, "Biden Win", "Trump Win")


# get the likelihood of each possible election outcome
b <- data.table(az=c(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
                ge=c(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
                fl=c(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
                mi=c(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
                nv=c(0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1),
                nc=c(0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1),
                pa=c(0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1),
                wi=c(1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1))

# read in the states
states <- fread("states.csv")
az <- pBETA(c(0.5), as.numeric(states[1,2])+1, as.numeric(states[1,3])+1)
ge <- pBETA(c(0.5), as.numeric(states[2,2])+1, as.numeric(states[2,3])+1)
fl <- pBETA(c(0.5), as.numeric(states[3,2])+1, as.numeric(states[3,3])+1)
mi <- pBETA(c(0.5), as.numeric(states[4,2])+1, as.numeric(states[4,3])+1)
nv <- pBETA(c(0.5), as.numeric(states[5,2])+1, as.numeric(states[5,3])+1)
nc <- pBETA(c(0.5), as.numeric(states[6,2])+1, as.numeric(states[6,3])+1)
pa <- pBETA(c(0.5), as.numeric(states[7,2])+1, as.numeric(states[7,3])+1)
wi <- pBETA(c(0.5), as.numeric(states[8,2])+1, as.numeric(states[8,3])+1)

b$az_p <- ifelse(b$az == 0, 1-az, az)
b$ge_p <- ifelse(b$ge == 0, 1-ge, ge)
b$fl_p <- ifelse(b$fl == 0, 1-fl, fl)
b$mi_p <- ifelse(b$mi == 0, 1-mi, mi)
b$nv_p <- ifelse(b$nv == 0, 1-nv, nv)
b$nc_p <- ifelse(b$nc == 0, 1-nc, nc)
b$pa_p <- ifelse(b$pa == 0, 1-pa, pa)
b$wi_p <- ifelse(b$wi == 0, 1-wi, wi)

b$Likelihood <- b$az_p * b$ge_p * b$fl_p * b$mi_p * b$nv_p * b$nc_p * b$pa_p * b$wi_p


data$Likelihood <- b$Likelihood

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

#####################################################
#
# CHANCE TRUMP WINS ELECTION USING STATES DATA
#
#####################################################
dem <- 226
rep <- 189

az_v <- 11
ge_v <- 16
fl_v <- 30
mi_v <- 15
nv_v <- 6
nc_v <- 16
pa_v <- 19
wi_v <- 10

b$votes <- b$az * az_v +
  b$ge * ge_v +
  b$fl * fl_v +
  b$mi * mi_v +
  b$nv * nv_v +
  b$nc * nc_v +
  b$pa * pa_v +
  b$wi * wi_v

b$trump_votes <- b$votes + rep
b$trump_win <- ifelse(b$trump_votes >= 270, 1, 0)
chance_of_trump_winning <- sum(b$trump_win * b$Likelihood)
chance_of_trump_winning
