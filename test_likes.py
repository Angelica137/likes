import unittest
from likes import likes


class LikesTest(unittest.TestCase):
    def test_list_empty(self):
        names = []
        self.assertEqual(likes(names), 'no one likes this')

    def test_one_person_likes(self):
        names = ["p"]
        self.assertEqual(likes(names), "p likes this")

    def test_2_ppl_like_this(self):
        names = ["p", "o"]
        self.assertEqual(likes(names), 'p and o like this')

    def test_3_ppl_like_this(self):
        names = ["p", "o", "o"]
        self.assertEqual(likes(names), 'p, o and o like this')

    def test_more_thatn_5_like_this(self):
        names = ["1", "2", "2", "3", "4"]
        self.assertEqual(likes(names), '1, 2 and 3 others like this')

    def test_more_that_10_like_this(self):
        names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.assertEqual(likes(names), '1, 2 and 8 others like this')


if __name__ == '__main__':
    unittest.main()
