# lib/helpers.py

from models.trainer import Trainer
from models.__init__ import CURSOR, CONN
from models.pokemon import Pokemon


def selected_trainer():
    trainer_select = input("Name of Pokemon Trainer: ")
    selected_trainer = Trainer.find_by_name(trainer_select)
    if selected_trainer:
           
           menu_pokemon(selected_trainer.name)      
    else:
        print("Selected trainer not found.")
        


def input_new_trainer():
    trainer_name = input("Please input the name of new pokemon trainer: ")
    existing_trainer = Trainer.find_by_name(trainer_name)
    if existing_trainer:
        print("Trainer name already exists. Please enter a non-listed name.")
    else:
        try:
            new_trainer = Trainer.create(trainer_name)
            print(f'{new_trainer.name} created.')
        except Exception as exc:
            print("Error creating pokemon trainer:", exc)

def delete_trainer():
    trainer_name = input("Name of pokemon trainer: ")
    trainer = Trainer.find_by_name(trainer_name)    
    if trainer:
        trainer.delete()
        print(f'Trainer {Trainer.name} deleted.')
    else:
        print(f'Trainer {trainer} not found.')

def selected_pokemon():
    pokemon_select = input("Name of capture pokemon: ")
    select_pokemon = Pokemon.find_by_name(pokemon_select)
    if select_pokemon:
       selected_pokemon_menu(select_pokemon)
    else:
        print("Selected Pokemon not found.")

def input_new_pokemon(selected_trainer):
    pokemon_name = input("Please input the name of new captured pokemon: ")
    existing_pokemon = Trainer.find_by_name(pokemon_name)
    if existing_pokemon:
        print("Pokemon has already been captured. Please enter a non-listed name.")
    else:
        try:
            pokemon_type = input("Please input type of new captured pokemon: ")
            pokemon_hp = input("Please input HP of new captured pokemon: ")
            hp = int(pokemon_hp)
            pokemon_attack = input("Please input attack of new captured pokemon: ")
            attack = int(pokemon_attack)
            pokemon_defense = input("Please input defense of new captured pokemon: ")
            defense = int(pokemon_defense)
            new_pokemon = Pokemon.create(selected_trainer, pokemon_name, pokemon_type, hp, attack, defense)
            
            print(f'{new_pokemon.pokemon_name} inputed.')
        except Exception as exc:
            print("Error inputing pokemon :", exc)

def update_pokemon():
    pass

def delete_pokemon():
    pass

def pokemon_menu(selected_trainer):
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(f"                             {selected_trainer}'s POKEMON:                            ")
    print("                                                                         ")    
    #Pokemon.drop_table()
    Pokemon.create_table()
    pokemons = Pokemon.find_by_trainer_name(selected_trainer)
    for pokemon in pokemons:
        print(pokemon.pokemon_name)

    print("                                                     ")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("                                                     ")
    print(" Please select an option from the menu:")
    print("     1. View Pokemon.")
    print("     2. Input A New Pokemon.")
    print("     3. Update Pokemon.")
    print("     4. Delete Pokemon.")
    print("     0. Exit to Pokemon Trainers' Menu.")
    print("                                                     ")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("                                                     ")    

def menu_pokemon(selected_trainer):
    while True:
        pokemon_menu(selected_trainer)
        pokemon_choice = input("> ")
        if pokemon_choice == "1":
            #list_pokemon()
            selected_pokemon()
        elif pokemon_choice == "2":
            #list_pokemon()
            input_new_pokemon(selected_trainer)
        elif pokemon_choice == "3":
            #list_pokemon()
            update_pokemon()
        elif pokemon_choice == "4":
            #list_pokemon()
            delete_pokemon()
        elif pokemon_choice == "0":
            break
        else:
            print("Invalid option, please select an option from the menu.")

def trainers_menu():
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("                             POKEMON TRAINERS                            ")
    print("                                                                         ")
    Trainer.create_table()
    trainers = Trainer.get_all()
    for trainer in trainers:
        print(trainer.name)
    print("                                                     ")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("                                                     ")
    print(" Please select an option from the menu:")
    print("     A. View Pokemon Trainer.")
    print("     B. Input A New Pokemon Trainer.")
    print("     C. Delete A Pokemon Trainer.")
    print("     D. Exit To Main Menu.")
    print("                                                     ")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("                                                     ")

def selected_pokemon_menu(select_pokemon):
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    for pokemon in select_pokemon:
        print(f"                             {pokemon.pokemon_name}:                            ")
        print("                                                                         ")
        print(f"TYPE: {pokemon.pokemon_type}.")
        print(f"HP: {pokemon.pokemon_hp}.")
        print(f"ATTACK: {pokemon.pokemon_attack}.")
        print(f"DEFENSE: {pokemon.pokemon_defense}.")

def exit_program():
    print("Goodbye!")
    exit()
