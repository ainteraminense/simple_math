"""Simple Math

This script get two inputs of the user and do mathematics operations. For each one it will return the result and print to the user.

This file can also be imported as a module and contains the following functions:

    * ask_user_input - return the input entered as string
    * convert_to_number - return the string input as int
    * sum - return the sum of two numbers
    * minus - return the subtraction of two numbers
    * multiply - return the multiplication of two numbers
    * divide - return the division of two numbers
"""


def ask_user_input(question: str) -> str:
    return input(question)


def convert_to_number(number_string):
    try:
        return int(number_string)
    except ValueError:
        return print("Error. Please enter a valid digit")


def sum(number1, number2):
    return number1 + number2


def main():
    question = "What is the first number? "
    user_input1_string = ask_user_input(question)
    user_input1_number = convert_to_number(user_input1_string)
    question = "What is the second number? "
    user_input2_string = ask_user_input(question)
    user_input2_number = convert_to_number(user_input2_string)
    print(f"{user_input1_string} + {user_input2_string} = {sum(user_input1_number, user_input2_number)}")

if(__name__ == '__main__'):
    main()
