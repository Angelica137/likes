import unittest
from likes import likes


class LikesTest(unittest.TestCase):
    def test_list_empty(self):
        names = []
        self.assertEqual(likes(names), 'no one likes this')


if __name__ == '__main__':
    unittest.main()
