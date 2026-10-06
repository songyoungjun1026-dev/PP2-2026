# 작성자: 송영준
# 작성일: 2026-10-03
# 문제: 고양이를 클래스로 정의하고 몇 개의 인스턴스를 생성해보자. 접근자와 설정자를 사용해보자 
# 클래스: Cat
# 인스턴스 변수와 자료형: name(str), age(int)
# 이름 접근자/설정자: getName(), setName()
# 나이 접근자/설정자: getAge(), setAge()

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age


def test_prob1():
    missy = Cat('Missy', 3)
    lucky = Cat('Lucky', 5)
    print(missy)
    print(lucky)

if __name__ == "__main__":
    test_prob1()