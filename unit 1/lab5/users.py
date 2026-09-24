class user:
    def _init_(self, id_user, name):
        self.id =id_user
        self.name = name

    def show_user_info(self):
        return f"user ID: {self.id}, user name: {self.name}"