"""3
Titanic Survivors analysis

"""
import utils as u

"""
dictionary with default commands
"""

commands = {"exit": u.exit_analysis,
            "default commands": u.print_commands,
            "Age histogram": u.show_hist,
            "Display as table": u.display_as_table
            }

kwargs = {"file_path": ["utils", "data", "train.csv"],
          "delimiter": ",",
          "hist_attr": "Age",
          "ylabel": "No. of passengers",
          "xlabel": "Titanic's passengers age",
          "exit": "exit",
          "read_commands": u.read_commands,
          "commands_dict": commands
          }


def main():
    number_of_runs = 0
    status_check = 0  # commands["exit"]()
    while status_check != 1:
        if number_of_runs == 0:
            print("Welcome to Titanic Analysis, following default commands are available:")
            u.print_commands(**kwargs)
            number_of_runs += 1
            continue
        else:
            run_command = input("Please type in your command:")
            try:
                status_check = commands[run_command](**kwargs)
                number_of_runs += 1
            except Exception as e:
                print(e)


if __name__ == '__main__':
    main()
