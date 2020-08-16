import static
import inventories
import ssh_connection


def general():
    print(static.MENU)
    for key in inventories.servers.keys():
        print(key)

    attempts_count = 1
    while attempts_count <= 3:
        try:
            input_serv = input("Choose needed server:  ")
        except KeyboardInterrupt:
            print(static.KEYBOARD_INTERRUPT_MESSAGE)
            exit()
        except ValueError:
            print("Error! You enter bad type argument. Try again")
            attempts_count += 1
        else:
            if input_serv in inventories.servers.keys():
                ssh_connection.new_connection(input_serv)
            else:
                print("You enter wrong server. Try again")
                attempts_count += 1
                continue
    else:
        print("You enter wrong argument 3 times. Exiting")
        exit()
