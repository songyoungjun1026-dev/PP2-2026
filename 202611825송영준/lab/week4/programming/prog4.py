# 작성자: 송영준
# 작성일: 2026-10-03
# 문제: 사각형을 나타내는 Rectangle 클래스를 작성하여 보자.
#       Rectangle 클래스는 다음과 같은 인스턴스 변수와 메소드를 가진다.
# 클래스: Rectangle
# 인스턴스 변수: x, y (좌측 상단 좌표), width, height (너비와 높이)
# 생성자: x, y, w, h를 각각 x, y, width, height 속성에 저장한다.
# 문자열 표현: 좌표와 크기를 나타내는 문자열 반환
# 접근자/설정자: 네 속성 각각에 대해 작성
# getArea: 면적 반환
# overlap: 다른 사각형과 겹치면 True, 아니면 False 반환


class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def __str__(self):
        return f"Rectangle(x={self.x}, y={self.y}, width={self.width}, height={self.height})"

    def setX(self, x):
        self.x = x

    def getX(self):
        return self.x

    def setY(self, y):
        self.y = y

    def getY(self):
        return self.y

    def setWidth(self, width):
        self.width = width

    def getWidth(self):
        return self.width

    def setHeight(self, height):
        self.height = height

    def getHeight(self):
        return self.height

    def getArea(self):
        return self.width * self.height

    def overlap(self, r):
        x_overlap = max(0, min(self.x + self.width, r.x + r.width) - max(self.x, r.x))
        y_overlap = max(0, min(self.y + self.height, r.y + r.height) - max(self.y, r.y))
        return x_overlap * y_overlap > 0


def test_prob4():
    r1 = Rectangle(0, 0, 100, 100)
    r2 = Rectangle(10, 10, 100, 100)
    if r1.overlap(r2):
        print("r1과 r2는 서로 겹칩니다.")
    else:
        print("r1과 r2는 서로 겹치지 않습니다.")


if __name__ == "__main__":
    test_prob4()