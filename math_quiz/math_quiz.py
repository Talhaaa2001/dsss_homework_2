import random
def function_for_integer(min_value, max_value):
    """
    It will develop a random integer within the specified range.
    """
    return random.randint(min_value, max_value)

def function_for_operator():
    """
    It will develop a random arithmetic operator: +, -, or *.
    """
    return random.choice(['+', '-', '*'])

def function_for_operation(operand1, operand2, operator):
    """
    It will performs the arithmetic operation based on the provided operator.
    Returns a tuple with the problem string and the correct answer.
    """
    problem = f"{operand1} {operator} {operand2}"
    if operator == '+':
        answer = operand1 + operand2
    elif operator == '-':
        answer = operand1 - operand2
    else:
        answer = operand1 * operand2
    return problem, answer

def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = function_for_integer(1, 10)
        num2 = function_for_integer(1, 5)
        operator = function_for_operator()  # Fix: Correct function name

        problem, correct_answer = function_for_operation(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()