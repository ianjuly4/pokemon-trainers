import sqlite3

CONN = sqlite3.connect('PokemonTrainers.db')
CURSOR = CONN.cursor()
