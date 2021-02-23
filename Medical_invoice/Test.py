class Person:
    def __init__(self,initialAge):
        self.initialAge = initialAge
        self.check = 0
        if self.initialAge < 0:
            self.Age = 0
            print("Age is not valid, setting age to 0")
        else:
            self.Age = initialAge
        # Add some more code to run some checks on initialAge
    def amIOld(self):
        if self.Age < 13:
            print("You are young.")
        elif self.Age >= 13 and self.Age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        self.Age += 1
        self.check += 1
        return self.Age


t = 4
for i in range(0, t):
    age = int(10)
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")