import uuid

class UserProfile:
    
    def __init__(self, name, email):
        self.hash_id = uuid.uuid4().hex
        self.name = name
        self.email = email


class User:
    
    def __init__(self, phone, user_profile):
        self.phone = phone 
    
    
    def update_phone(self, phone):
        
        
class PhoneBook(User):
    pass
