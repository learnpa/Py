class Vehicle:
    def general_usage(self):
        print("Transportation")


class car(Vehicle):
    def __init__(self):
        print("I'm car")
        self.wheels = 4
        self.has_roof = True


def specific_usage(self):
    self.general_usage()
    print("Specific usage is", "drive to office & vacation with family")


c = car()
specific_usage(c)
