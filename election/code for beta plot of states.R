library(data.table)
library(ggplot2)


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
