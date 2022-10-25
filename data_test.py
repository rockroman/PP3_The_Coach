import unittest
from data import user_score


class TestUserScore(unittest.TestCase):
    """
    test user score function
    with inputs
    """
    def test_user_score_valid(self):
        self.assertEqual(user_score(0), 0)
        self.assertEqual(user_score(23), 23)
        self.assertEqual(user_score(85.8), 85.8)

    def test_user_score_type(self):
        val = ""
        with self.assertRaises(TypeError):
            self.assertEqual(user_score(val), "")


if __name__ == '__main__':
    unittest.main()
