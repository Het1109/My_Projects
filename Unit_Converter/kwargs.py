# def calculate(n,m , **kwargs):
#     # for key, value in kwargs.items():
#     #     print(key , "=" ,value)
#     # print(kwargs["add"])
#     print(kwargs)
#     n += kwargs["add"]
#     print(f"addition : {n} ")
#     m *= kwargs["multiply"]
#     print(f"multplication : {m} ")
#
#
#
# calculate(10 , 10 ,add = 3 , multiply = 5 )



class Car:
    def __init__(self , **kwargs):
        self.name = kwargs["name"]
        self.model = kwargs["model"]

        print(f"{self.name} : {self.model}")

my_car = Car(name = "Nissian" , model= "GT-R")










