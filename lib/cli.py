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
                trainer_choice = input("> ")  
                if trainer_choice == "A":
                    selected_trainer()
                    list_trainers()
                elif trainer_choice == "B":
                    input_new_trainer()
                    list_trainers()
                elif trainer_choice == "C":
                    delete_trainer()
                    list_trainers()
                elif trainer_choice == "D":
                    break
                else:
                    print("Invalid option, please select an option from the menu.")
        
        elif choice == "0":
            exit_program()
        else:
            print("Invalid choice, please select a choice from the given menu.")





def menu():
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("                                                     ")
    print("  Hello, and Welcome to the Pokemon Trainers' Index.")
    print("  Please select an option from the menu:")
    print("  1. List of Pokemon Trainers")
    print("  0. Exit Pokemon Trainers")
    print("                                                     ")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    
   


def trainers_menu():
    print("                                                     ")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("                                                     ")
    print(" Please select an option from the menu:")
    print("     A. Select a pokemon trainer to view their pokemon.")
    print("     B. Input a new pokemon trainer.")
    print("     C. Delete a pokemon trainer.")
    print("     D. Exit to main menu.")
    print("                                                     ")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("                                                     ")



if __name__ == "__main__":
    main()
