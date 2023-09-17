import abc

DUMP_FILE = "./dump_file.dump"


class Logger(abc.ABC):
    
    def write_log(self, key:str, value:str):
        self.data[key] = value
        self.separator = "\n"
        self.fp = open(DUMP_FILE, "a")
        self.fp.write(key + self.separator + value + self.separator)
    
    def reload(self):
        self.separator = "\n"
        data = {}
        key = None
        with open(DUMP_FILE, 'r') as f:
            for temp in f:
                if temp == self.separator:
                    continue
                if not key:
                    key = temp
                else:
                    data[key[:-1]] = temp[:-1]
                    key = None
        return data

class Database(Logger):
    
    def __init__(self):
        self.data = self.reload()
        print(self.data)
        
    def get(self, key:str):
        return self.data[key]
    
    def write(self, key:str, value:str):
        self.data[key] = value
        self.write_log(key, value)

                
    
db = Database()
db.write("name", "ashutopsh")
print(db.get("name"))