# lib/cli.py

from helpers import (
    exit_program,
    #list_trainers,
    selected_trainer,
    input_new_trainer,
    delete_trainer,
    trainers_menu,
    pokemon_menu,
    selected_pokemon,
    input_new_pokemon,
    update_pokemon,
    delete_pokemon
)
def main():
    while True:
        menu()
        choice = input("> ")
        #list_trainers()
        if choice == "1":
            #list_trainers()
            while True:
                #list_trainers()
                trainers_menu()
                trainer_choice = input("> ")  
                if trainer_choice == "A":
                    selected_trainer()
                elif trainer_choice == "B":
                    input_new_trainer()
                    #list_trainers()
                elif trainer_choice == "C":
                    delete_trainer()
                    #list_trainers()
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
    print("  1. View Pokemon Trainers.")
    print("  0. Exit.")
    print("                                                     ")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    
   


#def trainers_menu():
    #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    #print("                             POKEMON TRAINERS                            ")
    #print("                                                                         ")
    #Trainer.create_table()
    #trainers = Trainer.get_all()
    #for trainer in trainers:
        #print(trainer.name)
    #print("                                                     ")
    #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    #print("                                                     ")
    #print(" Please select an option from the menu:")
    #print("     A. View Pokemon Trainer.")
    #print("     B. Input A New Pokemon Trainer.")
    #print("     C. Delete A Pokemon Trainer.")
    #print("     D. Exit To Main Menu.")
    #print("                                                     ")
    #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    #print("                                                     ")

#def pokemon_menu():
    #print("                                                     ")
    #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    #print("                                                     ")
    #print(" Please select an option from the menu:")
    #print("     1. View Pokemon.")
    #print("     2. Input A New Pokemon.")
    #print("     3. Update Pokemon.")
    #print("     4. Delete Pokemon.")
    #print("     0. Exit to Pokemon Trainers' Menu.")
    #print("                                                     ")
    #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    #print("                                                     ")    

if __name__ == "__main__":
    main()
