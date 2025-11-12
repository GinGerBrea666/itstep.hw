class Student:
    def __init__(self, major):
        self.major = major
        print(f"Ініціалізація: Студент, спеціальність: {self.major}")

    def study(self):
        print(f"Я сиджу і вчуся... (спеціальність: {self.major})")



class Worker:
    def __init__(self, job_title):
        self.job_title = job_title
        print(f"Ініціалізація: Працівник, посада: {self.job_title}")

    def work(self):
        print(f"Я працюю, заробляю гроші! (посада: {self.job_title}) ")

class StudentWorker(Student, Worker):

    def __init__(self, name, major, job_title):
        self.name = name
        print(f"\nСтворення '{self.name}':")

        Student.__init__(self, major)
        Worker.__init__(self, job_title)

    def describe(self):
        print("\n Хто я?")
        print(f"Я {self.name}.")
        print(f"Моя спеціальність: {self.major}")
        print(f"Моя посада: {self.job_title}")


