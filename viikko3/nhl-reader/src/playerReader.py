import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url

        url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
        response = requests.get(url).json()
        #response will have:
        #name
        #nationality 
        #assists
        #goals
        #penalties
        #team
        #games

        print("JSON-muotoinen vastaus:")
        print(response)
        self.players = []
        for player_dict in response:
            player = Player(
                player_dict['name'],
                player_dict['nationality'],
                player_dict['assists'],
                player_dict['goals'],
                player_dict['penalties'],
                player_dict['team'],
                player_dict['games']
            )

            self.players.append(player)
