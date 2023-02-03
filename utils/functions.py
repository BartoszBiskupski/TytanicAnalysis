from utils.classes import FileDataset
from utils.classes import SurvivalModel



def exit_analysis(**kwargs):
    """Exits the program."""
    command = kwargs["exit"]
    if command == "exit":
        print("Thank you for using the Titanic Analysis. Bye.")
        return 1
    else:
        return 0


def read_commands(commands_dict={}):
    """Lists all available default commands and in the Titanic Analysis program"""
    return_dict = {}
    for key in commands_dict:
        return_dict[key] = commands_dict[key].__doc__
    return return_dict


def print_commands(**kwargs):
    """Lists all available default commands and in the Titanic Analysis program"""
    commands_dscr = kwargs["read_commands"](kwargs["commands_dict"])

    print("Command Number: Short Description")
    for key, value in commands_dscr.items():
        print("{}: {}".format(key, value))


# def cleanup(**kwargs):
#     """Removes unpacked files"""
#     for path in os.listdir(**kwargs):
#         file_name = Path("utils") / "data" / path
#         os.remove(file_name)
#         print("File: {} was removed successfully".format(path))
#

def show_hist(**kwargs):
    """Displays histogram for Age category"""
    obj = FileDataset(**kwargs)
    return obj.hist()


def show_coeff(**kwargs):
    """Displays coefficient bar chart for most impactful features for passengers survivability."""
    obj = SurvivalModel(**kwargs)
    print("Based on regression model you have higher chances of survival "
          "if you are a female and a ticket from 1st class \n "
          "Most impactful feature determining survival rate of a passenger is sex"
          )
    return obj.plot_coefficients()


def display_as_table(**kwargs):
    """Display data as a table"""
    obj = FileDataset(**kwargs)
    return obj.display_table()


def update_pass_dict(dictionary={}):
    test_input = True
    for key in dictionary.keys():
        value = input(f"please type in your {key}: ")
        while test_input:
            try:
                value = int(value)
                dictionary[key] = value
                test_input = False
            except Exception:
                print("Incorrect value, please provide a number")
                value = input(f"please type in your {key}: ")
    return dictionary


def check_surv(**kwargs):
    """To check your survival chances, provide your:
        TicketClass: (1 = 1st class / 2 = 2nd class / 3 = 3rd class),
        PassengerAge: (1 - female, 0 - male),
        Age: (min=0 / max = 99),
        NumberOfSiblings: (number of related passengers min=0 / max=8),
        Fare: (number representing ticket price min=0 / max = 512)
        Values provided outside min/max will result in weaker predictions!
    """
    print(check_surv.__doc__)
    pass_dict = update_pass_dict(kwargs["pass_dict"])
    obj = SurvivalModel(**kwargs)
    print(obj.predict_proba(pass_dict))








