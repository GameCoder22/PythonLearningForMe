# this is my first module
# this is about users

# the class
class User:
#   how many users
    active_users = 0
#   the init
    def __init__(self,username,first, last, age):
        self.username = username
        self.first_name = first
        self.last_name = last
        self.age = age
        User.active_users += 1
# the repr
    def __repr__(self):
        return f"{self.username} is {self.first_name} {self.last_name}. He/she is {self.age}."


# these are the class methods
    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} users on."

    @classmethod
    def eztype(cls, data_str):
        username, first, last, age = data_str.split(", ")
        return cls(username, first, last, int(age))

# post alert

    def post(self, post):
        self.post = post
        return f"{self.username} posted '{self.post}'"

# their full name

    def name_display(self):
        return f'{self.first_name} {self.last_name}'

# their public real name

    def public_real_name_display(self):
        return f"{self.first_name[0]}.{self.last_name}"

# users likes

    def likes(self, things):
        return f"{self.username} likes {things}"

# big for things?

    def is_big_for_alot(self):
        return self.age >= 10

# birthday

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th birthday, {self.first_name}!"

# logout

    def logout(self):
        User.active_users -= 1
        return f"{self.username} has loged out."

# for mod

class Moderator(User):
    # how many mods
    mods = 0
    def __init__(self, username,first, last, age, community):
        super().__init__(username, first, last, age)
        self.community = community

    # how many mods active
    @classmethod
    def display_active_mods(cls):
        return f"There are currently {cls.mods} moderators on."

# allowed to remove post
    def remove_post(self):
        return f"{self.username} (a moderator) removed a post"











































