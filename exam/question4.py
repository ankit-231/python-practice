listNumber = [3, 2, 5, 7, 9, 8, 6, 0, 1, 4]


# The last digit number of my student ID is 4.


def function1(listN):
    """
    Parameter: listN
    Return: sum of last three elements
    """

    # extract last three elements from listN
    last_three_elements = listN[-3:]

    # get the sum of last three elements
    sum_of_last_three_elements = sum(last_three_elements)

    # return sum_of_last_three_elements
    return sum_of_last_three_elements


resultFromF1 = function1(listNumber)


def function2(resultFromF1):
    """
    Parameter: resultFromF1
    Return: None

    Displays unordered list of:
    • Return value of function1 is {resultFromF1}
    • User has three choices to guess the correct value
    • User got the correct answer/User did not get the correct answer
    """

    # variable to store status of user got the correct answer
    user_got_correct = False
    for i in range(3):
        # get user input
        user_input = input("Guess the correct value: ")
        try:
            # convert user input to int and compare with resultFromF1
            if int(user_input) == resultFromF1:
                user_got_correct = True
        except:
            # if cannot convert to int, let it be
            pass

    print(f"• Return value of function1 is {resultFromF1}")
    print(f"• User has three choices to guess the correct value")
    if user_got_correct:
        print(f"• User got the correct answer")
    else:
        print(f"• User did not get the correct answer")


function2(resultFromF1)
