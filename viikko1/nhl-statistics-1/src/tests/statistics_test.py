import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    def test_konstructori_asettaa_pelaajat_oikein(self):
        players =  PlayerReaderStub().get_players()
        self.assertEqual(self.statistics._players[0].name, "Semenko" )
        self.assertEqual(self.statistics._players[1].name, "Lemieux" )
        self.assertEqual(self.statistics._players[2].name, "Kurri" )
        self.assertEqual(self.statistics._players[3].name, "Yzerman" )
        self.assertEqual(self.statistics._players[4].name,"Gretzky" )
    
    def test_search_plalauttaa_oikean_pelaajan(self):
        self.assertEqual(self.statistics.search("S").name, "Semenko")
        self.assertEqual(self.statistics.search("er").name, "Yzerman")
        self.assertIsNone(self.statistics.search("-1"))
    
    def test_team_palauttaa_oikeat_pelaajat(self):
        players = self.statistics.team('PIT')
        self.assertEqual(players[0].name, "Lemieux")
        players = self.statistics.team('EDM')
        self.assertEqual(players[0].name, "Semenko")
        self.assertEqual(players[1].name, "Kurri")
        self.assertEqual(players[2].name, "Gretzky")
   
    def test_top_palauttaa_pelaajat_oikeassa_jarjestyksessa(self):
        players = self.statistics.top(4)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")
        self.assertEqual(players[2].name, "Yzerman")
        self.assertEqual(players[3].name, "Kurri")
        self.assertEqual(players[4].name, "Semenko")

   
