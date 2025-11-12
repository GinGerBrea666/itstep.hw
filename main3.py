import random
class Animal:
    def __init__(self, name, energy=100, hunger=0):
        self.name = name
        self.energy = energy
        self.hunger = hunger
        print(f"З'явилася тварина: {self.name}!")

    def eat(self):
        print(f"{self.name} їсть.")
        self.hunger -= 40
        if self.hunger < 0:
            self.hunger = 0

    def sleep(self):
        print(f"{self.name} спить... zzz...")
        self.energy = 100
        self.hunger += 10



class Dog(Animal):
    def __init__(self, name, breed, energy=100, hunger=0):

        super().__init__(name, energy, hunger)
        self.breed = breed
        print(f"Це {self.breed}.")

    def play_fetch(self):
        if self.energy > 30:
            print(f"{self.name} бавиться і приносить палицю!")
            self.energy -= 30
            self.hunger += 20
        else:
            print(f"{self.name} занадто втомився, щоб грати")

    def bark(self):
        print(f"{self.name} гавкає: Гав-гав!")


    def live_day(self):
        print(f"\n--- Новий день для {self.name} ---")


        if self.hunger > 70:
            print(f"{self.name} дуже голодний!")
            self.eat()
        elif self.energy < 40:
            print(f"{self.name} виснажений")
            self.sleep()
        else:

            action = random.choice(['play', 'bark', 'nothing'])
            if action == 'play':
                self.play_fetch()
            elif action == 'bark':
                self.bark()
            else:
                print(f"{self.name} бігає за тобою")

        # Природні зміни за день
        self.energy -= 10
        self.hunger += 15

        print(f"Стан: Енергія = {self.energy}, Голод = {self.hunger}")



my_dog = Dog(name="Рекс", breed="Вівчарка", energy=80, hunger=20)


for day in range(1, 4):
    print(f"\n=== ДЕНЬ {day} ===")
    my_dog.live_day()