"""
Titanic Survivors analysis

"""
import utils as u

"""
dictionary with default commands
"""
commands = {"exit": u.exit_analysis,
            "unpack": u.unpack_data,
            "default commands": u.read_commands,
            "cleanup": u.cleanup,
            "display data": u.display_table
            }
commands_dscr = commands["default commands"](commands_dict=commands)


def print_commands():
    print("Command: Short Description")
    for key, value in commands_dscr.items():
        print("{}: {}".format(key, value))


def main():
    number_of_runs = 0
    status_check = 0  # commands["exit"]()
    while status_check == 0:
        if number_of_runs == 0:
            print("Welcome to Titanic Analysis, following default commands are available:")
            print_commands()
            number_of_runs += 1
            continue
        else:
            run_command = input("Please type in your command:")
            try:
                if run_command == "exit":
                    status_check = commands[run_command](run_command)
                elif run_command == "default commands":
                    print_commands()
                else:
                    commands[run_command](run_command)
                number_of_runs += 1
            except Exception as e:
                print(e)


if __name__ == '__main__':
    main()
