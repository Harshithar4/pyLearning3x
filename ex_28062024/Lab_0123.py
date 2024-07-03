class Login:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login_confirm(self):
        if self.password == "Password123":
            print("Allowed")

        else:
            print("Not Allowed")
login=Login("gani@gmail.com","Password123")
login.login_confirm()