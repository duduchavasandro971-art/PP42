class User:
    # Class attribute
    status = "Active"

    def __init__(self, username, email, age):
        # Instance attributes
        self.username = username
        self.email = email
        self.age = age

    def get_info(self):
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Status: {self.status}")
        print("-" * 30)


# Create two user objects
user1 = User("alice123", "alice@example.com", 25)
user2 = User("bob456", "bob@example.com", 30)

# Display information for each user
user1.get_info()
user2.get_info()

# Check the class attribute
print("User 1 status:", user1.status)
print("User 2 status:", user2.status)