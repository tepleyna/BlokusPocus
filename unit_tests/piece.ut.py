import unittest, sys

sys.path.append("../")
sys.path.append("../..")
from BlokusPocus.app.piece import Piece

class TestBasicFunction(unittest.TestCase):
    # def setUp(self):
    #     self.func = ClassGoesHere()

    def test(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
