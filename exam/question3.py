valid_home_cat = ["house", "apartment", "mobilehome"]

valid_home_own = ["owned", "mortgaged", "rented", "hotel", "occupied"]

BREAK_WORD = "END"


def is_posint(number):
    """
    Parameter: number
    Return: True if number is a positive integer, False if it is not positive or if it is not convertible to integer
    """
    try:
        # convert input to int
        number = int(number)
    except:
        # if cannot convert to int, return False
        return False
    if number > 0:
        # if number is not positive, return False
        return True
    else:
        # if number is positive, return True
        return False


def get_home_category():
    """
    Parameter: None
    Return:
        "END" if user wants enters "END"
        home category in lowercase if valid, else keeps on asking for input until valid input is provided or "END" is entered
    """
    print(
        'HINT: \n \
                "house" (has space between any neighbouring homes)\n \
                "apartment" (is connected to neighbouring homes)\n \
                "mobileHome" (includes caravan, tent, or cardboard box).\n\n'
    )
    while True:
        # ask user for home category
        home_category = input(f"Please write your home category: {valid_home_cat}: ")
        # if user enters "END", return "END"
        if home_category == BREAK_WORD:
            return home_category
        # if user enters valid home category, return home category in lowercase
        if home_category.lower() in valid_home_cat:
            return home_category.lower()
        # if user enters invalid home category, print warning and keep on asking for input until valid input is provided or "END" is entered
        else:
            print("WARNING: Invalid home category. Please try again.\n")
            continue


def get_home_ownership():
    """
    Parameter: None
    Return: home ownership in lowercase
    """
    # print hint
    print(
        'HINT: \n \
                "Owned" (Owned by you or someone in this household free and clear)\n \
                "Mortgaged" (Owned by you or someone in this household with a mortgage or loan)\n \
                "Rented" (Regular payments are made to the owner or his/her agent)\n \
                "Hotel" (An apartment rented for 10 days or less)\n \
                "Occupied" (Nobody at this location owns the property or pays rent)\n'
    )
    while True:
        # ask user for home ownership
        home_ownership = input(f"Please write your home ownership: {valid_home_own}: ")
        # if user enters valid home ownership, return home ownership in lowercase
        if home_ownership.lower() in valid_home_own:
            return home_ownership.lower()
        # if user enters invalid home ownership, print warning and keep on asking for input until valid input is provided
        else:
            print("WARNING: Invalid home ownership. Please try again.\n\n")
            continue


def get_num_persons():
    """
    Parameter: None
    Return: number of persons in int
    """
    # print hint
    print(
        "HINT: \n \
            How many people (living human beings) are living or staying in this home (house, apartment, or mobile home)."
    )
    while True:

        # ask user for number of persons
        num_persons = input("Please write number of persons: ")

        # if user enters valid number of persons, return number of persons
        if is_posint(num_persons):
            return int(num_persons)

        # if user enters invalid number of persons, print warning and keep on asking for input until valid input is provided
        else:
            print("WARNING:Invalid number of persons. Please try again.\n")
            continue


def get_num_females(num_persons):
    """
    Parameter: None
    Return: number of females in int
    """
    # print hint
    remaining_persons = int(num_persons)
    print(
        f"HINT: \n \
            The number of female persons living in this household.\n \
            Remaining persons are {remaining_persons}.\n\n"
    )
    while True:

        # ask user for number of females
        num_females = input("Please write number of females: ")

        # if user enters valid number of females
        if is_posint(num_females):
            # if number of females is greater than remaining persons, print warning and keep on asking for input until valid input is provided
            if int(num_females) > remaining_persons:
                print(
                    "WARNING: Invalid number of females. It is greater than number of persons. Please try again.\n"
                )
                continue
            # if number of females is less than or equal to remaining persons, return number of females
            else:
                return int(num_females)

        # if user enters invalid number of females, print warning and keep on asking for input until valid input is provided
        else:
            print("WARNING: Invalid number of females. Please try again.\n")
            continue


def get_num_males(num_persons, num_females):
    """
    Parameter: None
    Return: number of males in int
    """
    # print hint
    remaining_persons = int(num_persons) - int(num_females)
    print(
        f"HINT: The number of male persons living in this household.\n \
            Remaining persons are {remaining_persons}.\n\n"
    )
    while True:

        # ask user for number of males
        num_males = input("Please write number of males: ")

        # if user enters valid number of males
        if is_posint(num_males):
            # if number of males is greater than remaining persons, print warning and keep on asking for input until valid input is provided
            if int(num_males) > remaining_persons:
                print(
                    f"WARNING: Invalid number of males. It is greater than number of persons minus number of females, i.e. {remaining_persons} Please try again.\n"
                )
                continue
            # if number of males is less than or equal to remaining persons, return number of males
            else:
                return int(num_males)

        # if user enters invalid number of males, print warning and keep on asking for input until valid input is provided
        else:
            print("WARNING: Invalid number of males. Please try again.\n")
            continue


def get_num_children(num_persons, num_females, num_males):
    """
    Parameter: None
    Return: number of children in int
    """
    # print hint
    remaining_persons = int(num_persons) - int(num_females) - int(num_males)
    print(
        f"HINT: The number of young individuals (<18 years old) living in this household.\n \
            Remaining persons are {remaining_persons}.\n\n"
    )
    while True:

        # ask user for number of children
        num_children = input("Please write number of children: ")
        if is_posint(num_children):
            # if number of children is greater than remaining persons, print warning and keep on asking for input until valid input is provided
            if int(num_children) > remaining_persons:
                print(
                    f"Invalid number of children. It is greater than number of persons minus number of females and males, i.e. {remaining_persons} Please try again."
                )
                continue
            # if number of children is less than or equal to remaining persons, return number of children
            else:
                return int(num_children)

        # if user enters invalid number of children, print warning and keep on asking for input until valid input is provided
        else:
            print("Invalid number of children. Please try again.")
            continue


def get_total_income():
    """
    Parameter: None
    Return: total income in int
    """
    # print hint
    print(
        "HINT: The sum of all people's annual salary in this home that provides funds for the household's running."
    )
    while True:

        # ask user for total income
        total_income = input("Please write total income: ")

        # if user enters valid total income return total income in int
        if is_posint(total_income):
            return int(total_income)

        # if user enters invalid total income, print warning and keep on asking for input until valid input is provided
        else:
            print("WARNING: Invalid total income. Please try again.")
            continue


def main():
    while True:
        # print hint
        print("HINT: Type 'END' if you want to exit.")

        # get home category
        home_category = get_home_category()

        # if user enters "END", exit
        if home_category == "END":
            print("Thank you for using this program.")
            break

        # get home ownership
        home_ownership = get_home_ownership()

        # get number of persons
        num_persons = get_num_persons()

        # get number of females
        num_females = get_num_females(num_persons)

        # get number of males
        num_males = get_num_males(num_persons, num_females)

        # get number of children
        num_children = get_num_children(num_persons, num_females, num_males)

        # get total income
        total_income = get_total_income()

        # display home ownership, home category, number of persons, number of females, number of males, number of children, and total income
        display(
            home_ownership,
            home_category,
            num_persons,
            num_females,
            num_males,
            num_children,
            total_income,
        )


def display(
    home_ownership,
    home_category,
    num_persons,
    num_females,
    num_males,
    num_children,
    total_income,
):
    """
    Parameter: home_ownership, home_category, num_persons, num_females, num_males, num_children, total_income
    Return: None

    Displays home ownership, home category, number of persons, number of females, number of males, number of children, and total income
    """
    print("\n\n")

    # print headings
    print(
        "{:<20}{:<20}{:<20}{:<20}{:<20}".format(
            "Home Ownership",
            "Home Category",
            "Num_Persons",
            "Num_Females",
            "Num_Males",
            "Num_Children",
            "Total_Income",
        )
    )

    # print lines
    print(
        "{:<20}{:<20}{:<20}{:<20}{:<20}".format(
            "______________",
            "_____________",
            "___________",
            "___________",
            "_________",
            "____________",
            "____________",
        )
    )

    # print the parameters
    print(
        "{:<20}{:<20}{:<20}{:<20}{:<20}".format(
            home_ownership,
            home_category,
            num_persons,
            num_females,
            num_males,
            num_children,
            total_income,
        )
    )
    print("\n\n")


main()
