class Human:
    def __init__(self, age, height, name="John"):
        self.age = age
        self.height = height
        self.name = name


class Student(Human):
    def __init__(self, age=16, height=175, name="John", money=100):
        super().__init__(age, height, name)
        self.money = money

    def work(self):
        print(f"{self.name} працює")
        self.money += 50

    def rest(self):
        print(f"{self.name} відпочиває")
        self.money -= 20

    def study(self):
        print(f"{self.name} навчається")
        self.money -= 10

    def live_year(self):
        for month in range(1, 13):
            print(f"\n--- Місяць {month} ---")
            if self.money < 30:
                self.work()
            else:
                self.study()
                self.rest()
            print(f"Гроші: {self.money} грн")


