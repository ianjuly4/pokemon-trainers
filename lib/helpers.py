# lib/helpers.py

from models.trainer import Trainer
from models.__init__ import CURSOR, CONN
from models.pokemon import Pokemon

def list_trainers():
    
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("                             POKEMON TRAINERS                            ")
    print("                                                                         ")

    Trainer.create_table()
    print([trainer.name for trainer in Trainer.get_all()])

def selected_trainer():
    trainer_select = input("Name of pokemon trainer: ")
    selected_trainer = Trainer.find_by_name(trainer_select)
    if selected_trainer:
       return [pokemon for pokemon in Trainer.all if pokemon.trainer == trainer_select]
    else:
        print("error")

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


def exit_program():
    print("Goodbye!")
    exit()
