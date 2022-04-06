class Animal:
    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print("Inhale, Exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Underwater!")

    def swim(self):
        print("Moving in water.")

nemo = Fish()
nemo1 = Animal()
nemo1.breathe()
nemo.breathe()