class student():
    def __init__(self, name, age, genre):
        self.name = name
        self.age = age
        self.genre = genre

    def __str__(self):
        if self.genre == "boy":
            return "His name is %s, and he is %d years old" % (self.name, self.age)

        elif self.genre == "girl":

            return "His name is %s, and she is %d years old" % (self.name, self.age)


s1 = student("Tommy", 19, "boy")
print(s1)

