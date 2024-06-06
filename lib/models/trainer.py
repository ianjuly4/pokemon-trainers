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
            CREATE TABLE if not exists trainers(
            id INTEGER PRIMARY KEY,
            name TEXT
            )
        """
        
    @classmethod
    def drop_table(cls):
        pass
    def save(self):
        pass

    @classmethod
    def create(cls, category_name):
      pass
    def update(self):
       pass
   
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