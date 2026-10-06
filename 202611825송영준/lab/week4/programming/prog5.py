# 작성자: 송영준
# 작성일: 2026-10-03
# 문제: 삼각형을 나타내는 클래스 Triangle를 작성해보자.
# 클래스: Triangle
# 인스턴스 변수: angle1, angle2, angle3, numberOfSides
# 생성자: 세 각도를 전달받아 저장하고 변의 개수는 기본값 3으로 저장한다.
# 문자열 표현: 삼각형 정보를 담은 문자열 반환
# 접근자/설정자: 각 속성의 값을 읽거나 저장한다.
# checkAngles(): 세 내각의 합이 180도인지 비교하여 T/F 반환

class Triangle:
    def __init__(self, a1, a2, a3, numberOfSides=3):
        self.angle1 = a1
        self.angle2 = a2
        self.angle3 = a3
        self.numberOfSides = numberOfSides

    def __str__(self):
        return (
            f"Triangle(angle1={self.angle1}, angle2={self.angle2}, "
            f"angle3={self.angle3}, numberOfSides={self.numberOfSides})"
        )

    def setAngle1(self, a1):
        self.angle1 = a1

    def getAngle1(self):
        return self.angle1

    def setAngle2(self, a2):
        self.angle2 = a2

    def getAngle2(self):
        return self.angle2

    def setAngle3(self, a3):
        self.angle3 = a3

    def getAngle3(self):
        return self.angle3

    def setNumberOfSides(self, numberOfSides):
        self.numberOfSides = numberOfSides

    def getNumberOfSides(self):
        return self.numberOfSides

    def checkAngles(self):
        return self.angle1 + self.angle2 + self.angle3 == 180


def test_prob5():
    triangle = Triangle(90, 30, 60)
    print(triangle.checkAngles())


if __name__ == "__main__":
    test_prob5()