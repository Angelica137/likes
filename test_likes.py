import unittest
from likes import likes


class LikesTest(unittest.TestCase):
    def test_list_empty(self):
        names = []
        self.assertEqual(likes(names), 'no one likes this')

    def test_one_person_likes(self):
        names = ["p"]
        self.assertEqual(likes(names), "p likes this")

if __name__ == '__main__':
    unittest.main()
