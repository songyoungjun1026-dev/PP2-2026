# 작성자: 송영준
# 작성일: 2026-10-03
# 문제: 상자를 나타내는 Box 클래스를 작성하여 보자.
#       Box 클래스는 가로길이, 세로길이, 높이를 나타내는 인스턴스 변수를 가진다.
# 클래스: Box
# 인스턴스 변수: length, height, depth
# 생성자: l, h, d를 각각 length, height, depth 속성에 저장한다.
# 접근자/설정자: 각 속성의 get 메서드는 값을 반환하고 set 메서드는 값을 저장한다.


class Box:
    def __init__(self, l, h, d):
        self.length = l
        self.height = h
        self.depth = d

    def __str__(self):
        return f"({self.length}, {self.height}, {self.depth})"

    def setLength(self, length):
        self.length = length

    def getLength(self):
        return self.length

    def setHeight(self, height):
        self.height = height

    def getHeight(self):
        return self.height

    def setDepth(self, depth):
        self.depth = depth

    def getDepth(self):
        return self.depth


def test_prob3():
    b1 = Box(100, 100, 100)
    b1.setHeight(100)
    b1.setLength(100)
    b1.setDepth(100)
    print(b1)
    print("상자의 부피는", b1.getHeight() * b1.getLength() * b1.getDepth())


if __name__ == "__main__":
    test_prob3()
