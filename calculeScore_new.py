import unittest

import calculeScore as c
class MyFirstTests(unittest.TestCase):


    def test_ScoreJoseph(self):
        self.assertEqual(c.test_calculerScore("Joseph",'15'),"66%")

    def test_ScoreMarie(self):
        self.assertEqual(c.test_calculerScore("Marie",'33'),"50%")

    def test_ScoreMarc(self):
        self.assertEqual(c.test_calculerScore("Marc",'60'),"43%")

    def test_ScoreEly(self):
        self.assertEqual(c.test_calculerScore("Ely",'28'),"75%")
