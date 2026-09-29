class Student:
    def __init__(self, name=None, age=0):
        self.__name = name
        self.__age = age

    def setAge(self, age):
        self.__age = age

    def setName(self, name):
        self.__name = name


obj = Student("Hong", 20)

print(obj.getName())
print(obj.getAge())
