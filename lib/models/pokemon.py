from models. __init__ import CURSOR, CONN
from models. trainer import Trainer

class Pokemon:
    def __init__(self, pokemon_name, pokemon_type, trainer_name, id=None):
        self.pokemon_name = pokemon_name
        self.pokemon_type = pokemon_type
        self.id = id
        self.trainer_name = trainer_name
    
    @property
    def pokemon_name(self):
        return self._pokemon_name
    @pokemon_name.setter
    def pokemon_name(self, pokemon_name):
        if isinstance(pokemon_name, str) and len(pokemon_name) >= 3:
            self._pokemon_name = pokemon_name
        else:
            raise TypeError("Pokemon name must be a string and have atleast 3 characters.")
        
    @property
    def pokemon_type(self):
        return self._pokemon_type
    @pokemon_type.setter
    def pokemon_type(self, pokemon_type):
        if isinstance(pokemon_type, str) and len(pokemon_type) >= 3:
            self._pokemon_type = pokemon_type
        else:
            raise TypeError("Pokemon type must be a string and have atleast 3 characters.")

    @property
    def trainer_name(self):
        return self._trainer_name
    @trainer_name.setter
    def trainer_id(self, trainer_name):
        if isinstance(trainer_name, str) and Trainer.find_by_name(trainer_name):
            self._trainer_name = trainer_name
        else:
            raise TypeError("Trainer name must be a string and reference a trainer in the database. ")
        
        


    