class Student:
    def __init__(self, name, surname, age, marks):
        self.name = name
        self.surname = surname
        self.age = age
        self.marks = marks
    def __str__(self) -> str:
        return f'\tName: {self.name}\n\tSurname: {self.surname}\n\tAge: {self.age}\n\tMarks: {self.marks}'
    
student = Student('Dmytro', 'Radchenko', '18', '12, 12, 11')

print(student)
print('---------------------------------')
class Car:
    def __init__(self, brand, model, speed, creation_date) -> None:
        self.brand = brand
        self.model = model
        self.speed = speed
        self.creation_date = creation_date
    def __str__(self) -> str:
        return f'\tBrand: {self.brand}\n\tModel: {self.model}\n\tSpeed: {self.speed}\n\tCreation date: {self.creation_date}'
    
car = Car('Toyota', 'Camry 3.5', '300', '2021')

print(car)