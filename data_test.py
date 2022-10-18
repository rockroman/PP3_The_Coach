import unittest
from data import user_score


class Test_user_score(unittest.TestCase):
    """
    test user score function
    with inputs
    """
    def test_user_score_valid(self):
        self.assertEqual(user_score(6), 6)


if __name__ == '__main__':
    unittest.main()
