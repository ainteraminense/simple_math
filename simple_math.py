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
    # this function receive a string with a question
    # it uses that question to get a user input
    # return the user input
    return input(question)


def main():
    question = "What is the first number? "
    user_input_string = ask_user_input(question)


# if(__name__ == "__main__"):
#     main()
if(__name__ == '__main__'):
    main()
