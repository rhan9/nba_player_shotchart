"""
Author: Ryan Han
Date Updated: 5/7/2020

Description: This script asks for a player's full name, team, and a specific year.
Once inputted, the script will access NBA game statistics through 'nba_api',API Client for www.nba.com
and produce a detailed Pandas dataframe of regular season field goal attempts
by the specified player during the specified NBA year.

Input: NBA player's full name, current team, and NBA season start year
Output: Pandas DataFrame
"""


###############################################################################
# IMPORT MODULES                                                              #
###############################################################################
from nba_api.stats.static import players
from nba_api.stats.static import teams
from nba_api.stats.endpoints import shotchartdetail as scd


###############################################################################
# FUNCTIONS                                                                   #
###############################################################################
# Input: 'full name'
# Output: dictionary consisting of player info such as player id
def player_info(fullname):
    player_dict = players.get_players()
    for player in player_dict:
        if player['full_name'] == fullname:
            return(player)


# Input:'team name'
# Output: dictionary consisting of team info such as team id and year_founded
def team_info(teamname):
    nba_teams = teams.get_teams()
    for team in nba_teams:
        if team['full_name'] == teamname:
            return(team)


# Input: Pandas DataFrame
# Output: cleaned up DataFrame
# Checks that data in dataframe is unique and that there are no missing values
def clean_df(df):
    df = df.drop_duplicates()
    df.dropna(inplace=True)
    clean_df = df[['PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM_NAME', 'SHOT_ZONE_BASIC',
                   'SHOT_ZONE_AREA', 'SHOT_ZONE_RANGE', 'SHOT_DISTANCE',
                   'LOC_X', 'LOC_Y', 'SHOT_MADE_FLAG', 'GAME_DATE']]
    clean_df = clean_df.rename(columns={'PLAYER_ID': 'id', 'PLAYER_NAME': 'name', 'TEAM_ID': 'team_id', 'TEAM_NAME': 'team_name',
                                        'SHOT_ZONE_BASIC': 'shot_zone_basic', 'SHOT_ZONE_AREA': 'shot_zone_area',
                                        'SHOT_ZONE_RANGE': 'shot_zone_range', 'SHOT_DISTANCE': 'shot_distance',
                                        'LOC_X': 'x', 'LOC_Y': 'y', 'SHOT_MADE_FLAG': 'shot_made', 'GAME_DATE': 'game_date'})
    return(clean_df)


# Input: Year
# Output: Stats dataframe separated by year
# Since NBA seasons start in one year and end in the next, had to include 'year + 1'
# Range is for NBA regular season usually starting in Oct. and ending by May
def separate_year_charts(year):
    chart_by_year = shotchart_df[(shotchart_df['game_date'] > (str(year) + '1001')) &
                                 (shotchart_df['game_date'] < (str(year + 1) + '0531'))]
    return(chart_by_year)


###############################################################################
# MAIN                                                                        #
###############################################################################
# inputs to variables
fullname = input("Please input the full name of the player: ")
teamname = input("Please input the full name of this player's current team: ")
year = input("Please input start year for NBA season: ")

# run functions using input variables and assign them to variables
player = player_info(fullname.title())
team = team_info(teamname.title())

# Accessing NBA stats using ShotChartDetail endpoint
# Two arguments must be passed through: player_id and team_id
# Use dictionary keys to access player and team id
# Emphasis 'context_measure_simple="FGA"' to get all Field Goal Attempts(FGA)
# not just 'makes'
stats = scd.ShotChartDetail(player_id=player['id'],
                            team_id=team['id'], context_measure_simple="FGA")
# use .get_data_frames[0] method to access shot chart data
shots_df = stats.get_data_frames()[0]

# get rid of columns we don't need
shotchart_df = clean_df(shots_df)

# output: stats needed to make a shotchart for a specific year
shotchart = separate_year_charts(int(year))
print(shotchart)
