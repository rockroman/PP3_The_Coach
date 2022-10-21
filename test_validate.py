import unittest
from validate import display_menu
from unittest.mock import patch


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


class TestDisplayMenu(unittest.TestCase):
    """
    testing  for user input   
    between two options offered
    """
    @patch('builtins.input', return_value='a')
    def test_display_menu_good_input(self, mock_input):
        result = display_menu
        self.assertEqual(result,'a')


if __name__ == '__main__':
    unittest.main()
