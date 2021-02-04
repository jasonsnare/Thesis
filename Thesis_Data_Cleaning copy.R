library(tidyverse)

#Read in files
game_data <- read_csv('games.csv')
teams <- read_csv('teams.csv')
def_2020 = read.csv("d2020 - Sheet1.csv")
def_2019 = read.csv("d2019 - Sheet1.csv")
def_2018 = read.csv("d2018 - Sheet1.csv")
def_2017 = read.csv("d2017 - Sheet1.csv")
def_2016 = read.csv("d2016 - Sheet1.csv")
def_2015 = read.csv("d2015 - Sheet1.csv")
def_2020 = subset(def_2020, select = -c(X))
def_2019 = subset(def_2019, select = -c(X))
def_2018 = subset(def_2018, select = -c(X))
def_2017 = subset(def_2017, select = -c(X))
def_2016 = subset(def_2016, select = -c(X))

#Join game and team data
games_teams <- full_join(game_data, teams,
                         by = c("HOME_TEAM_ID" = "TEAM_ID"))
games_teams <- full_join(games_teams, teams,
                         by = c('VISITOR_TEAM_ID' = 'TEAM_ID'))

#Break data down by year to add defensive data
games_2015 <- games_teams %>% filter(SEASON == 2015)
games_2016 <- games_teams %>% filter(SEASON == 2016)
games_2017 <- games_teams %>% filter(SEASON == 2017)
games_2018 <- games_teams %>% filter(SEASON == 2018)
games_2019 <- games_teams %>% filter(SEASON == 2019)
games_2020 <- games_teams %>% filter(SEASON == 2020)

#Join defensive data
complete_2015 <- full_join(games_2015, def_2015,
                           by = c('NICKNAME.x' = 'TEAM'))
complete_2015 <- full_join(complete_2015, def_2015,
                           by = c('NICKNAME.y' = 'TEAM'))
complete_2016 <- full_join(games_2016, def_2016,
                           by = c('NICKNAME.x' = 'TEAM'))
complete_2016 <- full_join(complete_2016, def_2016,
                           by = c('NICKNAME.y' = 'TEAM'))
complete_2017 <- full_join(games_2017, def_2017,
                           by = c('NICKNAME.x' = 'TEAM'))
complete_2017 <- full_join(complete_2017, def_2017,
                           by = c('NICKNAME.y' = 'TEAM'))
complete_2018 <- full_join(games_2018, def_2018,
                           by = c('NICKNAME.x' = 'TEAM'))
complete_2018 <- full_join(complete_2018, def_2018,
                           by = c('NICKNAME.y' = 'TEAM'))
complete_2019 <- full_join(games_2019, def_2019,
                           by = c('NICKNAME.x' = 'TEAM'))
complete_2019 <- full_join(complete_2019, def_2019,
                           by = c('NICKNAME.y' = 'TEAM'))
complete_2020 <- full_join(games_2020, def_2020,
                           by = c('NICKNAME.x' = 'TEAM'))
complete_2020 <- full_join(complete_2020, def_2020,
                           by = c('NICKNAME.y' = 'TEAM'))

#Rejoin all data
final_df <- rbind(complete_2015, complete_2016)
final_df <- rbind(final_df, complete_2017)
final_df <- rbind(final_df, complete_2018)
final_df <- rbind(final_df, complete_2019)
final_df <- rbind(final_df, complete_2020)

#Drop unnecessary columns
final_df <- subset(final_df,
                   select = -c(GAME_DATE_EST, GAME_ID, GAME_STATUS_TEXT, 
                               HOME_TEAM_ID, VISITOR_TEAM_ID, TEAM_ID_home, 
                               TEAM_ID_away, LEAGUE_ID.x, LEAGUE_ID.y,
                               MIN_YEAR.x, MIN_YEAR.y, MAX_YEAR.x,
                               MAX_YEAR.y, YEARFOUNDED.x,
                               YEARFOUNDED.y, DLEAGUEAFFILIATION.x,
                               DLEAGUEAFFILIATION.y, HOME_TEAM_WINS,
                               ABBREVIATION.x, ABBREVIATION.y, NICKNAME.x, 
                               NICKNAME.y, CITY.x, CITY.y, ARENA.x, ARENA.y,
                               ARENACAPACITY.x, ARENACAPACITY.y, OWNER.x,
                               OWNER.y, GENERALMANAGER.x, GENERALMANAGER.y,
                               HEADCOACH.x, HEADCOACH.y, W.x, W.y,
                               L.x, L.y, GP.x, GP.y, MIN.x, MIN.y))

#write.csv(final_df,"Final_Thesis_DF.csv", row.names = FALSE)












