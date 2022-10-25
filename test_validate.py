import unittest
from unittest.mock import patch
from validate import display_menu


# code taken from question answered on stackoverflow!
class TestValidate(unittest.TestCase):
    """
    testing  is display menu function
    based on input calls the right function after
    """
    @patch("validate.new_user")
    @patch("builtins.input", return_value="a")
    def test_user_input_a(self, patched_input, patched_new_user):
        status = display_menu()
        self.assertEqual(status, "a")
        patched_new_user.assert_called()

    @patch("validate.exsisting_user")
    @patch("builtins.input", return_value="b")
    def test_user_input_b(self, patched_input, patched_exsisting_user):
        status = display_menu()
        self.assertEqual(status, "b")
        patched_exsisting_user.assert_called()


if __name__ == "__main__":
    unittest.main()
