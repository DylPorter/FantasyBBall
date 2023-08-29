import requests
import pandas
import json

# Load json file containing information pre-provided by user
with open('data.json') as json_data:
    init_info = json.load(json_data)
json_data.close()

# Assign json info to variables in order to make API requests
# Check if json values are not empty (user must self-initialise)
if ((init_info["year"] == "") or (init_info["league_id"] == "") \
        or (init_info["swid"] == "") or (init_info["espn_s2"] == "")):
    print("Please fill out all of the required fields in ./data.json")
    exit()

year = init_info["year"]
league_id = init_info["league_id"]
espn_cookies = {"swid": init_info["swid"], "espn_s2": init_info["espn_s2"]}

url = f"https://fantasy.espn.com/apis/v3/games/fba/seasons/{year}/segments/0/leagues/{league_id}"

###############################################################3
# FUNCTIONS
###############################################################3

def standings():
    r = requests.get(url, cookies=espn_cookies, params={"view": ["mTeam", "mTeam"]})
    raw_data = r.json()
    df = [[
            team['playoffSeed'],
            team['name'],
            team['record']['overall']['wins'],
            team['record']['overall']['losses'],
            team['record']['overall']['ties'],
            team['record']['overall']['percentage'],
            team['record']['overall']['gamesBack'],
        ] for team in raw_data['teams']]

    df = pandas.DataFrame(df, columns=['Position', 'Team', 'Wins', 'Losses', 'Ties', 'Win%', "Games Back"])
    df = df.sort_values(by=["Position"])
    
    print(df)
    

def team_list():
    r = requests.get(url, cookies=espn_cookies, params={"view": ["mTeam", "mTeam"]})
    raw_data = r.json()
    df = [[
            team['name'],
        ] for team in raw_data['teams']]

    df = pandas.DataFrame(df, columns=["Choose a team:"])

    print(df)


def roster(team_id): #mRoster
    r = requests.get(url, cookies=espn_cookies, params={"view": ["mTeam", "mRoster"]})
    raw_data = r.json()
    df = [[
            player['playerPoolEntry']['player']['fullName'],

            round(player['playerPoolEntry']['player']['stats'][0]['averageStats']['40'], 1), # MIN
            round(player['playerPoolEntry']['player']['stats'][0]['averageStats']['17'], 1), # 3PM
            round(player['playerPoolEntry']['player']['stats'][0]['averageStats']['6'], 1), # REB
            round(player['playerPoolEntry']['player']['stats'][0]['averageStats']['3'], 1), # AST
            round(player['playerPoolEntry']['player']['stats'][0]['averageStats']['2'], 1), # STL
            round(player['playerPoolEntry']['player']['stats'][0]['averageStats']['1'], 1), # BLK
            round(player['playerPoolEntry']['player']['stats'][0]['averageStats']['0'], 1), # PTS

            player['playerPoolEntry']['player']['injuryStatus'],
            round(player['playerPoolEntry']['player']['ownership']['percentOwned'], 3),
            round(player['playerPoolEntry']['player']['ownership']['percentChange'], 3),

        ] for player in raw_data['teams'][team_id]['roster']['entries']]

    df = pandas.DataFrame(df, columns=['Name', 'MIN', '3PM', 'REB', \
            'AST', 'STL', 'BLK', 'PTS', 'Status', '% Owned', '% Change'])

    print(df)

while True:
    choice = int(input("1. Standings\n2. Team Roster\n>>>  "))
    if choice == 1:
        standings()
    elif choice == 2:
        team_list()
        team_id = int(input(">>> "))
        roster(team_id)

