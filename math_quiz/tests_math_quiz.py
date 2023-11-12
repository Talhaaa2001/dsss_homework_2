import unittest
from math_quiz import function_for_integer, function_for_operator,function_for_operation

class TestMathGame(unittest.TestCase):

    def test_function_for_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num =function_for_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_for_operator(self):
        # Test if the random operator is one of '+', '-', or '*'
        valid_operators = {'+', '-', '*'}
        for _ in range(1000):  # Test a large number of random values
            rand_operator = function_for_operator()
            self.assertIn(rand_operator, valid_operators)

    def test_function_for_operation(self):
        test_cases = [
            (8, 1, '+', '8 + 1', 9),
            (9, 4, '-', '9 - 4', 5),
            (2, 3, '*', '2 * 3', 6),
            # Add more test cases as needed
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = function_for_operation(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()