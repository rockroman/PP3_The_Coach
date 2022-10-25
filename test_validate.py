import unittest
from unittest.mock import patch
from validate import display_menu
# from unittest import mock


# class TestDisplayMenu(unittest.TestCase):
#     """
#     testing  for user input   
#     between two options offered
#     """
#     def test_display_menu_good_input(self):
#         actual_input = 'b'
#         expected_input = ('a', 'b')
#         self.assertIn(actual_input, expected_input)

#     def test_display_menu_another_good_input(self):
#         actual_input = 'a'
#         expected_input = ('a', 'b')
#         self.assertIn(actual_input, expected_input)

#     def test_display_menu_another_invalid_input(self):
#         actual_input = 2
#         expected_input = ('a', 'b')
#         self.assertNotIn(actual_input, expected_input)

# # ----up working-----





class TestValidate(unittest.TestCase):
    """
    testing  for user input   
    between two options offered
    """
    @patch("validate.new_user")
    @patch("builtins.input", return_value="a") 
    def test_input_a(self, patched_input, patched_new_user):
        status = display_menu()
        self.assertEqual(status, "a")
        patched_new_user.assert_called()

    @patch("validate.exsisting_user")
    @patch("builtins.input", return_value="b")
    def test_input_b(self, patched_input, patched_exsisting_user):
        status = display_menu()
        self.assertEqual(status, "b")
        patched_exsisting_user.assert_called()


if __name__ == "__main__":
    unittest.main()


# class TestValidate(unittest.TestCase):
#     @patch("validate.exsisting_user")
#     @patch("validate.new_user")
#     @patch("builtins.input", return_value="a")
#     def test_a(self, patched_input, patched_new_user, patched_exsisting_user):
#         status = display_menu()

#         self.assertEqual(status, "a")
#         patched_new_user.assert_called()
#         patched_exsisting_user.assert_not_called()

#     @patch("validate.exsisting_user")
#     @patch("validate.new_user")
#     @patch("builtins.input", return_value="b")
#     def test_b(self, patched_input, patched_new_user, patched_exsisting_user):
#         status = display_menu()

#         self.assertEqual(status, "b")
#         patched_new_user.assert_not_called()
#         patched_exsisting_user.assert_called()
  

if __name__ == "__main__":
    unittest.main()

