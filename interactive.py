from os import system, name
import static
import ssh_connection
import functions


def start_interactive():
    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux
        else:
            _ = system('clear')

    def exit_from_checker():
        ssh_connection.Ssh.close_connection()
        print("Bye bye!")
        exit()

    while True:
        clear()
        print(static.FUNCTIONS_MENU)

        switcher = {
            1: functions.list_top_users,
            2: functions.delete_old_messages,
            3: exit_from_checker
        }

        def start_swich_func(inputed_func):
            func = switcher.get(inputed_func, "error")
            try:
                func()
            except TypeError:
                print("Function that you enter does not exist. Try again.")
                return False
            else:
                return True

        def input_chosen_func():
            attempts_count = 1
            while attempts_count <= 3:
                try:
                    input_func = int(input("Choose needed function:  "))
                except KeyboardInterrupt:
                    print(static.KEYBOARD_INTERRUPT_MESSAGE)
                    exit_from_checker()
                except ValueError:
                    print("Error! You enter not int argument. Try again")
                    attempts_count += 1
                else:
                    if start_swich_func(input_func):
                        break
                    else:
                        attempts_count += 1
                        continue
            else:
                print("You enter wrong argument 3 times. Exiting")
                exit_from_checker()

        input_chosen_func()



