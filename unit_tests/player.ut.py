import unittest, sys, copy

sys.path.append("../")
sys.path.append("../..")
from BlokusPocus.app.Player import Player

class TestPlayer(unittest.TestCase):
    def setUp(test):
        test.name = "Tracey"
        test.id = 1
        test.color = "red"
        test.player = Player(test.name, test.id, test.color)

    def testGetDisplayName(test):
        test.assertEqual(test.player.getDisplayName(), test.name)

    def testGetId(test):
        test.assertEqual(test.player.getId(), test.id)

    def testGetColor(test):
        test.assertEqual(test.player.getColor(), test.color)


class TestPlayerFactory(unittest.TestCase):
    def setUp(test):
        test.names = "Abby, Brett, Casey, Dad"

    def testNumberOfPlayers(test):
        for i in range(1,5):
            players = Player.playerFactory(i, test.names[0:i])
            test.assertEqual(len(players), i)
