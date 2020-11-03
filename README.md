# nba_player_shotchart
Contains files for final project in Data 440 - Spatial Data Discovery 

## README
* Updated: 5/07/2020
* Name: Ryan Han
* Github: rhan9
* Class: Data 440 - Spatial Data Discovery
* Topic: Final Project

### Files

#### process.txt
* Process of how project developed

#### player_shotchart.py
* This script asks for a player's full name, team, and a specific year. Once inputted, the script will access NBA game statistics through the nba_api and produce a detailed Pandas dataframe of regular season field goal attempts by the specified player during the specified NBA year.

* Variables created:
    * fullname
    * teamname
    * year
    * player
    * team
    * stats
    * shots_df
    * shotchart_df
    * shotchart

* Imports needed:
    * from nba_api.stats.static import players
    * from nba_api.stats.static import teams
    * from nba_api.stats.endpoints import shotchartdetail as scd

* How To Run:
    * This script requires you to install nba_api:
                pip install nba_api
    * More instructions can be found here: https://github.com/swar/nba_api.
    * Once installed, the script will ask you for a NBA players full name. The full name must be spelled correctly. I suggest visiting https://stats.nba.com/players/ and copying/ pasting players full name.
    * For team, I suggest inputting in the players most current team. Again visiting https://stats.nba.com/players/ and copying/pasting teams full name would be best.
    * For year, I suggest values from 2000 - 2019, as the data will be most accurate. The player must have played for the team during the year specified.

        Example input:
            * Please input the full name of the player: Giannis Antetokounmpo
            * Please input the full name of this player's current team: Milwaukee Bucks
            * Please input start year for NBA season: 2016
* Output:
    * A Pandas Dataframe with columns for 'id', 'name', 'team_id', 'team_name', 'shot_zone_basic', 'shot_zone_area', 'shot_zone_range', 'shot_distance', 'x', 'y','shot_made', 'game_date'

#### README.md
* This Readme file.
#### project_rhan9.Rmd
* R Markdown file that explains the project, describes the date and visualization process. 
#### shotchartoutput.ipynb
* Example jupyter notebook file that shows pandas dataframe output after player_shotchart.py was run and above 'example' inputted.


### Data Scources
* https://github.com/swar/nba_api
* https://stats.nba.com/player/203507/
* https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/endpoints/shotchartdetail.md

#### Data Attribution
* Description: I used the API Client package “nba_api”, to access my data. Nba_api is an API Client for www.nba.com and contains various api endpoints that can provide nba data to the user.
* Specifically I used the endpoint ‘shotchartdetail’ to access my data. Shotchardetail allowed me to access NBA stats data,that had recorded shot locations as longitude (X) latitude (Y) values for every shot a player took during a specific NBA regular season.
* Data Origin:
    * https://github.com/swar/nba_api/blob/master/README.md
    * https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/endpoints/shotchartdetail.md
* Definitions for Data Used:
    * PLAYER_ID
        * Each player's unique id number
        * Matches player id on www.nba.com
        * In script, renamed to 'id'
    * PLAYER_NAME
        * Each player's full name
        * In script, renamed to 'name'
    * TEAM_ID
        * Each team's unique id number
        * Matches team id on www.nba.com
        * In script, renamed to 'team_id'
    * TEAM_NAME
        * Each team's full name
        * In script, renamed to 'team_name'
    * LOC_X
        * Units from (0,0)
        * In my script, renamed to 'x'
        * For visual purposes, 10 units counted as 1 foot
    * LOC_Y
        * Units from (0,0)
        * In my script, renamed to 'y'
        * For visual purposes, 10 units counted as 1 foot
    * SHOT_MADE_FLAG
        * indicates made shot or missed shot
        * made shot = 1
        * missed shot = 0
        * In script, renamed to 'shot_made'
    * GAME_DATE
        * Follows YYYYMMDD format
        * In script, renamed to 'game_date'
* Contact Info:
    * Repo Creator: Swar Patel
    * github username: swar
* Date Created: 2018-09-18
* Last Updated: 2020-01-27
