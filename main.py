"""3
Titanic Survivors analysis

"""
import utils as u

"""dictionary with default commands"""
commands = {"99 - exit": u.exit_analysis,
            "1 - default commands": u.print_commands,
            "2 - Age histogram": u.show_hist,
            "3 - Coefficient bar plot": u.show_coeff,
            "4 - Display as table": u.display_as_table,
            "5 - Check your survival rate": u.check_surv
            }

"""passenger dictionary used to test chances of survival"""
passenger = {"TicketClass": 0,
             "Sex": 0,
             "PassengerAge": 0,
             "NumberOfSiblings": 0,
             "Fare": 0
             }

"""set of defualt arguments used in classes/functions"""
kwargs = {"file_path": ["utils", "data", "train.csv"],
          "delimiter": ",",
          "hist_attr": "PassengerAge",
          "ylabel": "No. of passengers",
          "xlabel": "Titanic's passengers age (binsize = 2y)",
          "exit": "exit",
          "read_commands": u.read_commands,
          "commands_dict": commands,
          "pass_dict": passenger
          }


def main():
    """main loop to display instructions and take input for user which command to run"""
    number_of_runs = 0
    status_check = 0
    #main loop. Exists only when user input == 99
    while status_check != 1:
        if number_of_runs == 0:
            print("Welcome to Titanic Analysis, following default commands are available:")
            u.print_commands(**kwargs)
            number_of_runs += 1
            continue
        else:
            run_command = input("Please type in your command:")
            try:
                # check to take only one kew from the commands dict, matching the input
                result = [key for key in commands if key.startswith(run_command)][0]
                status_check = commands[result](**kwargs)
                number_of_runs += 1
            except IndexError:
                print("No such command, for help type in ""1"" ")
                continue
            except Exception as e:
                print(f"Unexpected happened {e}")


if __name__ == '__main__':
    main()
