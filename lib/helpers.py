# lib/helpers.py

from models.trainer import Trainer
from models.__init__ import CURSOR, CONN
from models.pokemon import Pokemon

def list_trainers():
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("                             POKEMON TRAINERS                            ")
    print("                                                                         ")

    Trainer.create_table()
    trainers = Trainer.get_all()
    for trainer in trainers:
        print(trainer.name)

def input_new_trainer():
    trainer_name = input("Please input the name of new pokemon trainer: ")
    existing_trainer = Trainer.find_by_name(trainer_name)
    if existing_trainer:
        print("Trainer name already exists. Please enter a non-listed name.")
    else:
        try:
            new_trainer = Trainer.create(trainer_name)
            print(f'{new_trainer.trainer_name} created.')
        except Exception as exc:
            print("Error creating pokemon trainer:", exc)

def selected_category():
    category_select = input("Name of category: ")
    category_expense = Expense.find_by_category(category_select)
    if category_expense:
       for expense in category_expense:
           print(expense.expense_name, expense.expense_amount, expense.expense_month)
    elif category_expense != Expense.find_by_category(category_select):
        print("Selected category must reference a category in the categories database.")
    else:
        print("Selected category does not represent any current expense.")


def exit_program():
    print("Goodbye!")
    exit()
