class USER:
    def __init__(self, username, password, email):
        self.username = username
        self.__password = password
        self.email = email

    def show_user(self):
        print(f"User: {self.username}")


class POST:
    def __init__(self, topic, content, author):
        self.topic = topic
        self.content = content
        self.author = author

    def show_post(self):
        print(f"Topic: {self.topic}")
        print(f"Content: {self.content}")
        print(f"Author: {self.author.username}")


class COMMENT:
    def __init__(self, author, text, post):
        self.author = author
        self.text = text
        self.post = post

    def show_comment(self):
        print(f"{self.author.username}: {self.text}")
        print(f"Post: {self.post.topic}")


class MESSAGE:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content

    def show_message(self):
        print(f"From: {self.sender.username}")
        print(f"To: {self.receiver.username}")
        print(f"Message: {self.content}")


# USERS
user1 = USER("Raul", "1234", "raul@gmail.com")
user2 = USER("Joel", "5678", "joel@gmail.com")

# POST
post1 = POST(
    "Python OOP",
    "Classes and objects are important.",
    user1
)

# COMMENT
comment1 = COMMENT(
    user2,
    "Nice explanation!",
    post1
)

# MESSAGE
message1 = MESSAGE(
    user2,
    user1,
    "Can you explain inheritance?"
)

# SHOW DATA
post1.show_post()
print()

comment1.show_comment()
print()

message1.show_message()