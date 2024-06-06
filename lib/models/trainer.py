from models.__init__ import CURSOR, CONN
class Trainer:

    all = {}

    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 1:
            self._name = name
        else:
            raise ValueError("Category must be a string and have atleast 1 character.")

    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS trainers(
            id INTEGER PRIMARY KEY,
            name TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS trainers
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO trainers(name)
            VALUES(?)
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name):
      trainer = cls(name)
      trainer.save()
      return trainer

    def update(self):
        sql = """
            UPDATE trainers
            SET name = ?,
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()    
   
    @classmethod
    def instance_from_db(cls, row):
        pass
    @classmethod
    def get_all(cls):
      pass
    @classmethod
    def find_by_id(cls, id):
       pass
    
    @classmethod
    def find_by_name(cls, category_name):
      pass
    def get_expenses(self):
       pass
    def delete(self):
       pass