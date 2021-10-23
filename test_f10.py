import unittest
from main import f10

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(f10(100,1,[],8),[4,4,1])



