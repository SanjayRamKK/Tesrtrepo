class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, new_mail):
        if "@" in new_mail:
            self._email = new_mail

user1 = User("sanjay", "sanjay@gmail.com", "123")
user1.email = "hi"
print(user1.email)