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

bt_data <- candidate_data[candidate_data$Trump > 0]
#bt_data <- bt_data[bt_data$Harris > 0]
bt_data <- bt_data[,c("poll_id", "end_date", "sample_size", "population", "state",
                      "Biden", "Harris", "Trump", "DeSantis", "Kennedy", "West", 
                      "Haley", "Mapstead", "Manchin", "Newsom", "Pence", "Scott",
                      "Ramaswamy", "Cheney", "Christie", "Clinton", "Whitmer", 
                      "Sanders")]
bt_data

m <-lm(Harris~Biden+(factor(state)+factor(population))**2, data=bt_data)
summary(m)
bt_data$PREDICTION <- predict.lm(m, data=bt_data)
bt_data