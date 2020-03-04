import unittest, sys, copy

sys.path.append("../")
sys.path.append("../..")
from BlokusPocus.app.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(test):
        test.name = "Tracey"
        test.id = 1
        test.color = "red"
        test.player = Player(test.name, test.id, test.color)

    def testGetDisplayName(test):
        assertEqual(test.player.getDisplayName(), test.name)

    def testBlankDisplayName(test):
        assertEqual(test.player.getDisplayName(), test.name)
