# lib/helpers.py

from models.trainer import Trainer
from models.__init__ import CURSOR, CONN
from models.pokemon import Pokemon


def exit_program():
    print("Goodbye!")
    exit()
