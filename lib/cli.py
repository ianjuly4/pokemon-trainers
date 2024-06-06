# lib/cli.py

from helpers import (
    exit_program,
    list_trainers,
    selected_trainer,
    input_new_trainer,
    delete_trainer
)


def main():
    while True:
        menu()
        choice = input("> ")

        if choice == "1":
            list_trainers()
            while True:
                trainers_menu()
                trainers_choice = (">")
                if trainers_choice == "A":
                    selected_trainer()
                    list_trainers()
                elif trainers_choice == "B":
                    input_new_trainer
                elif trainers_choice == "c":
                    delete_trainer
                elif trainers_choice == "D":
                    break
        elif choice == "0":
            exit_program()
        else:
            print("Invalid choice, please select a choice from the given menu.")





def menu():
    print("Please select an option:")
    print("1. List of Pokemon Trainers")
    print("0. Exit Pokemon Trainers")

def trainers_menu():
    print("                                                     ")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("                                                     ")
    print(" Please select an option from the menu:")
    print("     A. Select a pokemon trainer to view their pokemon.")
    print("     B. Input a new pokemon trainer.")
    print("     C. Delete a pokemon trainer.")
    print("     D. Exit to main menu.")
    print("                                                     ")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("                                                     ")



if __name__ == "__main__":
    main()
