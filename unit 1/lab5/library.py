class library:
    def _init_(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_users(self, user):
            self.users.append(user)

    def show_book(self, book):
            for books in self.books:
                  print(book.show_nooks())