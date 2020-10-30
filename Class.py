class Human:
    def __init__(self, n, o):
        self.occupation = o
        self.name = n

    def do_work(self):
        if self.occupation == "Actor":
            print(self.name, "Acts in hollywood movie")
        elif self.occupation == "Tennis player":
            print(self.name, "Plays Tennis")

    def speaks(self):
        print(self.name, "Says Hi!")

tom = Human("Tom Cruise", "Actor")
tom.do_work()
tom.speaks()

maria = Human("Maria Sharapova", "Tennis player")
maria.do_work()
maria.speaks()
