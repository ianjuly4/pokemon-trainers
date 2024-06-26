# lib/helpers.py

from models.trainer import Trainer
from models.__init__ import CURSOR, CONN
from models.pokemon import Pokemon


def selected_trainer():
    str_trainer_select = input("Number of Pokemon Trainer: ")
    trainer_select = int(str_trainer_select)
    selected_trainer = Trainer.find_by_id(trainer_select)
    if selected_trainer:
           menu_pokemon(selected_trainer)      
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
    
        except Exception as exc:
            print("Error creating pokemon trainer:", exc)


def delete_trainer():
    str_trainer_id = input("Number of the Pokemon trainer: ")
    trainer_id = int(str_trainer_id)
    trainer = Trainer.find_by_id(trainer_id)
    if not trainer:
        print(f"Number {trainer_id} trainer not found.")
        return

    pokemons = trainer.pokemons()
    #if not pokemons:
        #print(f"No Pokémon found for trainer with ID {trainer_id}.")
        #return

    pokemons = trainer.pokemons()
    for pokemon in pokemons:
        pokemon.delete()

    trainer.delete()
    print(f"Number {trainer.name} trainer and their associated Pokemon have been deleted.")

def selected_pokemon(selected_trainer):
    pokemon_select = input("Name of captured pokemon: ")
    select_pokemon = Pokemon.find_by_name(pokemon_select)
    trainer = Trainer.find_by_id(selected_trainer.id)
    if trainer:
        if select_pokemon:
            if select_pokemon.trainer_id == trainer.id:
                pokemon_menu_selected(select_pokemon)
            else:
                print("Selected pokemon is not associated with current trainer.")
        else:
            print("Selected Pokemon not found.")
    else:
        print("Trainer not found.")
        

def input_new_pokemon(selected_trainer):
    pokemon_name = input("Please input the name of new captured pokemon: ")
    existing_pokemon = Pokemon.find_by_name(pokemon_name)
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
            new_pokemon = Pokemon.create(selected_trainer.id, pokemon_name, pokemon_type, hp, attack, defense)
            
            print(f'{new_pokemon.pokemon_name} inputed.')
        except Exception as exc:
            print("Error inputing pokemon :", exc)


def update_pokemon(select_pokemon):
            
            new_type = input("Please input Pokemon's new Type: ")
            select_pokemon.pokemon_type = new_type
            string_new_hp = input("Please input Pokemon's new HP: ")
            new_hp = int(string_new_hp)
            select_pokemon.pokemon_hp = new_hp
            string_new_attack = input("Please input Pokemon's new Attack: ")
            new_attack = int(string_new_attack)
            select_pokemon.pokemon_attack = new_attack
            string_new_defense = input("Please input Pokemon's new Defense: ")
            new_defense = int(string_new_defense)
            select_pokemon.pokemon_defense = new_defense
            select_pokemon.update()

def delete_pokemon(selected_trainer):
    pokemon_name = input("Name of pokemon: ")
    select_pokemon = Pokemon.find_by_name(pokemon_name)
    trainer = Trainer.find_by_id(selected_trainer.id)

    if trainer:
        if select_pokemon:
            if select_pokemon.trainer_id == trainer.id:
                select_pokemon.delete()
            else:
                print("Selected pokemon is not associated with current trainer.")
        else:
            print("Selected Pokemon not found.")
    else:
        print("Trainer not found.")


def pokemon_menu(selected_trainer):
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(f"                             {selected_trainer.name}'s POKEMON:                            ")
    print("                                                                         ")    
    #Pokemon.drop_table()
    Pokemon.create_table()
    pokemons = selected_trainer.pokemons()
    for i, pokemon in enumerate(pokemons, start=1):
        print(f'{i}. {pokemon.pokemon_name}')
    #for pokemon in pokemons:
        #print(pokemon.pokemon_name)
    print("                                                     ")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("                                                     ")
    print(" Please select an option from the menu:")
    print("     1. View Pokemon.")
    print("     2. Input A New Pokemon.")
    print("     3. Delete A Pokemon.")
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
            selected_pokemon(selected_trainer)
        elif pokemon_choice == "2":
            #list_pokemon()
            input_new_pokemon(selected_trainer)
        elif pokemon_choice == "3":
            #list_pokemon()
            delete_pokemon(selected_trainer)
        elif pokemon_choice == "0":
            break
        else:
            print("Invalid option, please select an option from the menu.")

def pokemon_menu_selected(select_pokemon):
    while True:
        selected_pokemon_menu(select_pokemon)
        selected_pokemon_choice = input("> ")
        if selected_pokemon_choice == "A":
            update_pokemon(select_pokemon)
        elif selected_pokemon_choice == "D":
            break
        else:
            print("Invalid option, please select an option from the menu.")

def trainers_menu():
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("                             POKEMON TRAINERS                            ")
    print("                                                                         ")
    #Trainer.drop_table()
    Trainer.create_table()
    trainers = Trainer.get_all()
    for i, trainer in enumerate(trainers, start=1):
        print(f'{i}. {trainer.name}')
    #for trainer in trainers:
        #print(trainer.name)
    #trainers = (trainer.name for trainer in Trainer.get_all())
    #print(trainers)
    print("                                                     ")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("                                                     ")
    print(" Please select an option from the menu:")
    print("     A. View Pokemon Trainer's Pokemon.")
    print("     B. Input A New Pokemon Trainer.")
    print("     C. Delete A Pokemon Trainer And Their Pokemon.")
    print("     D. Exit To Main Menu.")
    print("                                                     ")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("                                                     ")

def selected_pokemon_menu(select_pokemon):
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    print(f"                             {select_pokemon.pokemon_name}:                            ")
    print("                                                                         ")
    print(f"TYPE: {select_pokemon.pokemon_type}.")
    print(f"HP: {select_pokemon.pokemon_hp}.")
    print(f"ATTACK: {select_pokemon.pokemon_attack}.")
    print(f"DEFENSE: {select_pokemon.pokemon_defense}.")
    print("                                                     ")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("                                                     ")
    print(" Please select an option from the menu:")
    print(f"     A. Update {select_pokemon.pokemon_name}.")
    print("     D. Exit to Pokemon Menu.")
    print("                                                     ")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("                                                     ")   

def exit_program():
    print("Goodbye!")
    exit()
