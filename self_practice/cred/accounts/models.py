from typing import String


class UserProfile:
    __email: str = ""
    __phone: str = ""
    profile_photo:str = ""
    __name: str = ""

    def __init__(self) -> None:
        pass

    def update_email(self, email):
        pass

    def update_phone(self, phone):
        pass


class User(UserProfile):
    account_id:str = ""
    auth_token: str = "" # cur auth token for api calls

    profile: UserProfile = None

    def reset_password(self):
        pass
    
    def recover_account(self):
        pass


