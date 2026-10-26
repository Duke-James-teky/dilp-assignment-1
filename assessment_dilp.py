# class Account:
#     def __init__(self, balance):
#         self.__balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount

#     def get_balance(self):
#         return self.__balance

# a = Account(100)
# a.deposit(50)
# a.deposit(-20)
# print(a.get_balance())

# class Cat:
#     def speak(self):
#         return "Meow"

# class Dog:
#     def speak(self):
#         return "Woof"

# for animal in [Cat(), Dog()]:
#     print(animal.speak())

# class Car:
#     def __init__(self, brand):
#         brand = brand

# c = Car("toyota")
# print(c.brand)

# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed

# d = Dog("rex", "lab")
# print(d.name, d.breed)

# class Dog:
#     def __init__(self, name):
#         self.name = name

# d = Dog("rex")
# print(d.name)

# @app.get("/user_id")
# def get_user(user_id: int):
#     return {"user_id": user_id}


class Animal:
    def speak(self):
        return "sound"

class Cow(Animal):
    def speak(self):
        return "Moo"

print(Cow().speak())





