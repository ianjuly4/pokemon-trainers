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
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS pokemons(
            id INTEGER PRIMARY KEY,
            trainer_name TEXT,
            pokemon_name TEXT,
            pokemon_type TEXT,
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
            INSERT INTO pokemons(trainer_name, pokemon_name, pokemon_type)
            VALUES = (?,?,?)
        """
    
        CURSOR.execute(sql, (self.trainer_name, self.pokemon_name, self.pokemon_type))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE pokemons
            SET trainer_name, pokemon_name = ?, pokemon_type = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.trainer_name, self.pokemon_name,
                             self.pokemon_type, self.id))
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
    def create(cls, trainer_name, pokemon_name, pokemon_type):
        pokemon = cls(trainer_name, pokemon_name, pokemon_type)
        pokemon.save()
        return pokemon

    @classmethod
    def instance_from_db(cls, row):
        pokemon = cls.all.get(row[0])
        if pokemon:
            pokemon.trainer_name = row[1]
            pokemon.pokemon_name = row[2]
            pokemon.pokemon_type = row[3]
        else:
            pokemon = cls(row[1], row[2], row[3])
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
    def find_by_name(cls, name):
        pass
    

        


    