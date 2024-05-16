library(data.table)
library(lubridate)

data <- fread("president_polls(1).csv")
data

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
