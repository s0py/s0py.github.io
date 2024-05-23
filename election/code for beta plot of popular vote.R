library(data.table)
library(ggplot2)
library(ggthemes)

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