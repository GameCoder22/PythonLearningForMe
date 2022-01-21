class User:

    active_users = 0
#    posts = 0
    def __init__(self,username,first, last, age):
        self.username = username
        self.first_name = first
        self.last_name = last
        self.age = age
        User.active_users += 1

    def __repr__(self):
        return f"{self.username} is {self.first_name} {self.last_name}. He/she is {self.age}."



    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} users on."

    @classmethod
    def eztype(cls, data_str):
        username, first, last, age = data_str.split(", ")
        return cls(username, first, last, int(age))

#    @classmethod
#    def display_posts(self):
#       f"There are {self.posts} here."

    def post(self, post):
        self.post = post
        return f"{self.username} posted '{self.post}'"

    def name_display(self):
        return f'{self.first_name} {self.last_name}'

    def public_real_name_display(self):
        return f"{self.first_name[0]}.{self.last_name}"

    def likes(self, things):
        return f"{self.username} likes {things}"

    def is_big_for_alot(self):
        return self.age >= 10

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th birthday, {self.first_name}!"

    def logout(self):
        User.active_users -= 1
        return f"{self.username} has loged out."


class Moderator(User):
    mods = 0
    def __init__(self, username,first, last, age, community):
        super().__init__(username, first, last, age)
        self.community = community

    @classmethod
    def display_active_mods(cls):
        return f"There are currently {cls.mods} moderators on."

    def remove_post(self):
        return  f"{self.username} (a moderator) removed a post"



Nitro = Moderator("Nitrogamer", "Aaradhya", "Y.", 11, "Hydro")
Oxi = User("Oxigamer", "Gyanada", "Y.", 6)
Someone = User.eztype("user, name, last, 23")
print(Nitro.community)









