from books import book
from users import user
from library import library

book1 = book("001", "Python for dummies", "Emma Deras", "Deras")
book2 = book("002", "OOP for dummies", "coche rodiruges", "car")

user1 = user("001", "Emma Deras")

library.add_book(book1)
library.add_book(book2)

library.add_users(user1)

