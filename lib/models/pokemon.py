class Pokemon:
    def __init__(self, pokemon_name, pokemon_type, id=None):
        self.pokemon_name = pokemon_name
        self.pokemon_type = pokemon_type
        self.id = id
        self._trainer_id = None

    