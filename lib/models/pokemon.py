from models. __init__ import CURSOR, CONN
from models. trainer import Trainer

class Pokemon:

    all = {}

    def __init__(self, 
                trainer_name,
                pokemon_name, 
                pokemon_type, 
                pokemon_hp,
                pokemon_attack,
                pokemon_defense,
                id=None):
        self.pokemon_name = pokemon_name
        self.pokemon_type = pokemon_type
        self.id = id
        self.trainer_name = trainer_name
        self.pokemon_hp = pokemon_hp
        self.pokemon_attack = pokemon_attack
        self.pokemon_defense = pokemon_defense
    
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
    def trainer_name(self, trainer_name):
        if isinstance(trainer_name, str):
            self._trainer_name = trainer_name
        else:
            raise TypeError("Trainer name must be a string. ")
        
    @property
    def pokemon_hp(self):
        return self._pokemon_hp
    @pokemon_hp.setter
    def pokemon_hp(self, pokemon_hp):
        if isinstance(pokemon_hp, int):
            self._pokemon_hp = pokemon_hp
        else:
            raise TypeError("Pokemon HP must be an integer.")
    @property
    def pokemon_attack(self):
        return self._pokemon_attack
    @pokemon_attack.setter
    def pokemon_attack(self, pokemon_attack):
        if isinstance(pokemon_attack, int):
            self._pokemon_attack = pokemon_attack
        else:
            raise TypeError("Pokemon Attack must be an intger.")
    
    @property
    def pokemon_defense(self):
        return self._pokemon_defense
    @pokemon_defense.setter
    def pokemon_defense(self, pokemon_defense):
        if isinstance(pokemon_defense, int):
            self._pokemon_defense = pokemon_defense
        else:
            raise TypeError("Pokemon Defense must be an integer.")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS pokemons(
            id INTEGER PRIMARY KEY,
            trainer_name TEXT,
            pokemon_name TEXT,
            pokemon_type TEXT,
            pokemon_hp INTEGER,
            pokemon_attack INTEGER,
            pokemon_defense INTEGER,
            FOREIGN KEY (trainer_name) REFERENCES trainers (name)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS pokemons
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO pokemons(trainer_name, pokemon_name, pokemon_type, pokemon_hp, pokemon_attack, pokemon_defense)
            VALUES (?,?,?,?,?,?)
        """
    
        CURSOR.execute(sql, (self.trainer_name, self.pokemon_name, self.pokemon_type, self.pokemon_hp, self.pokemon_attack, self.pokemon_defense))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE pokemons
            SET trainer_name = ?, pokemon_name = ?, pokemon_type = ?, pokemon_hp = ?, pokemon_attack = ?, pokemon_defense = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.trainer_name, self.pokemon_name, self.pokemon_type, self.pokemon_hp, self.pokemon_attack, self.pokemon_defense, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM pokemons
            WHERE id  = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, trainer_name, pokemon_name, pokemon_type, pokemon_hp, pokemon_attack, pokemon_defense):
        pokemon = cls(trainer_name, pokemon_name, pokemon_type, pokemon_hp, pokemon_attack, pokemon_defense)
        pokemon.save()
        return pokemon

    @classmethod
    def instance_from_db(cls, row):
        pokemon = cls.all.get(row[0])
        if pokemon:
            pokemon.trainer_name = row[1]
            pokemon.pokemon_name = row[2]
            pokemon.pokemon_type = row[3]
            pokemon.pokemon_hp = row[4]
            pokemon.pokemon_attack = row[5]
            pokemon.pokemon_defense = row[6]
        else:
            pokemon = cls(row[1], row[2], row[3], row[4], row[5], row[6])
            pokemon.id = row[0]
            cls.all[pokemon.id] = pokemon
        return pokemon


    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM pokemons
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM pokemons
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, pokemon_name):
        sql = """
            SELECT *
            FROM pokemons
            WHERE pokemon_name = ?
        """

        rows = CURSOR.execute(sql, (pokemon_name,)).fetchall()
        if rows:
            return cls.instance_from_db(rows[0])
        else:
            return None
    
    @classmethod
    def find_by_trainer_name(cls, trainer_name):
        sql = """
            SELECT *
            FROM pokemons
            WHERE trainer_name = ?
        """
        rows = CURSOR.execute(sql, (trainer_name,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
        


    