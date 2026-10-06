# 작성자: 송영준
# 작성일: 2026-10-03
# 문제: 로켓을 나타내는 Rocket 클래스를 작성해보자.
#       Rocket 클래스는 다음과 같은 인스턴스 변수와 메소드를 가진다.
# 클래스: Rocket
# 인스턴스 변수: x, y
# 설계: moveUp()은 y좌표만 변경하고 x좌표는 유지한다.


class Rocket:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"로켓의 높이: {self.y}"

    def moveUp(self):
        self.y += 1


def test_prob2():
    myRocket = Rocket()
    print("로켓의 높이:", myRocket.y)

    myRocket.moveUp()
    print("로켓의 높이:", myRocket.y)


if __name__ == "__main__":
    test_prob2()