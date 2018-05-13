class User:

    active_users = 0

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def __repr__(self):
        return f"{self.first} is {self.age}"

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"

    def full_name(self):
        return f"{self.last}, {self.first}"

    def initials(self):
        return f"{self.first[0]}. {self.last}"

    def likes(self, thing):
        return f"likes {thing}."

    def is_senior(self):
        return f"Senior: {self.age >=65}"

    @classmethod
    def display_active_users(cls):
        return f"There are currently {User.active_users} active users"

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))



user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)

print(user1.first, user1.last, user1.age)
print(user1.full_name())
print(user1.initials())
print(user1.likes("Ice Cream"))
print(user1.is_senior())
print("==========")
print(user2.first, user2.last, user2.age)
print(user2.full_name())
print(user2.initials())
print(user2.likes("fast cars"))
print(user2.is_senior())
print("==========")
print(User.active_users)
print(User.display_active_users())
print("==========")
print(user2.logout())
print("==========")
print(User.active_users)
print(User.display_active_users())
print("==========")
print(User.from_string("Tom, Jones, 32").full_name())
print(User.display_active_users())
print("====__repr__======")
j=User("judy", "steele", 18)
j=str(j)
print(j)