library(data.table)
library(ggplot2)

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