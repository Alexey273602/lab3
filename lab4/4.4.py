class Car:
    counter = 0

    def __init__(self, name, speed, volume):
        self.name = name
        self.speed = speed
        self.volume = volume

    def show_info(self):
        print(f"Название: {self.name}")
        print(f"Максимальная скорость: {self.speed}")
        print(f"Объём двигателя: {self.volume}")

    def show_counter(self):
        print(f"Счётчик равен {self.counter}")

    @staticmethod
    def is_fast():
        if car.speed > 200:
            print(f"Машина достаточно быстрая")
        else:
            print(f"Машина не достаточно быстрая")

    @classmethod
    def iterator(cls):
        cls.counter += 1


car = Car("BMW", 120, 5.5)
car.show_info()
car.is_fast()
car.show_counter()
car.iterator()
car.show_counter()
