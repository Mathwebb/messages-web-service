class User:
    def __init__(self, user_id:int, user_name:str, email_address:str) -> None:
        self.user_id = user_id
        self.user_name = user_name
        self.email_address = email_address

    def __eq__(self, other) -> bool:
        return self.user_id == other.user_id

    def __str__(self) -> str:
        return f"User: {self.user_id} {self.user_name} {self.email_address}"

    def __repr__(self) -> str:
        return f"User: {self.user_id} {self.user_name} {self.email_address}"