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

data = json_load["response"]


def get_top_scorers():

    top_scorers = [{
        'name': '',
        'goals': '',
        'club': '',
        'profile_pic': ''
    }]


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

    return top_scorers