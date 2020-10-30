class Father:
    def skills(self):
        print("Cooking & Programming")


class Mother:
    def skills(self):
        print("Music & Fashion")


class Child(Mother, Father):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Dancing")


c = Child()
c.skills()
