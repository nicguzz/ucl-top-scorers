import requests
import json

url = "https://api-football-v1.p.rapidapi.com/v3/players/topscorers"

querystring = {"league":"2","season":"2021"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "f73950abdbmsh8ca5b99cfcea60dp1df00cjsnc775948a4277"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
json_load = response.json()

num = 0
# result = data["response"][3]['player']
data = json_load["response"]


# print("TOP 3 scorers from:")
# print(data[0]['statistics'][0]['league']['name'])
# print()


top_scorers = [{
    'name': '',
    'goals': '',
    'club': '',
    'profile_pic': ''
}]


    # print((f"[{num}]. ") + player['player']['name'])
    # print(str(player['statistics'][0]['goals']['total']) + " goals")
    # print(str(player['statistics'][0]['team']['name']))

    # top_scorers.update(player['player']['name'])

# top_scorers[0]['name'] = data[0]['player']['name']
# top_scorers[0]['goals'] = data[0]['statistics'][0]['goals']['total']
# top_scorers[0]['club'] = data[0]['statistics'][0]['team']['name']
# top_scorers[0]['profile_pic'] = data[0]['player']['photo']


num = 0


for player in data[0:10]:
    name = player['player']['name']
    goals = player['statistics'][0]['goals']['total']
    club = player['statistics'][0]['team']['name']
    player_photo = player['player']['photo']
    club_logo = player['statistics'][0]['team']['logo']

    if num < 1:


        top_scorers[num]['name'] = name
        top_scorers[num]['goals'] = goals
        top_scorers[num]['club'] = club
        top_scorers[num]['profile_pic'] = player_photo
        top_scorers[num]['club_logo'] = club_logo

        num = num + 1
    else:
        top_scorers.append({'name': f"{name}", 'goals': f"{goals}", 'club': f"{club}", 'profile_pic': f"{player_photo}", 'club_logo': f"{club_logo}"})
