# 작성자: 송영준
# 작성일: 2026-10-03
# 문제: Person이라는 클래스를 작성해보자.
# 클래스: Person
# 인스턴스 변수: name, mobile, office, email
# 휴대폰 번호, 직장 전화번호, 이메일은 None 기본값을 가진다.
# __str__: 이름과 연락처 정보를 담은 문자열을 반환한다.
# 접근자/설정자: 네 속성 각각의 값을 읽거나 변경한다.


class Person:
    def __init__(self, name, mobile=None, office=None, email=None):
        self.name = name
        self.mobile = mobile
        self.office = office
        self.email = email

    def __str__(self):
        return (
            f"Person(name={self.name}, mobile={self.mobile}, "
            f"office={self.office}, email={self.email})"
        )

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setMobile(self, mobile):
        self.mobile = mobile

    def getMobile(self):
        return self.mobile

    def setOffice(self, office):
        self.office = office

    def getOffice(self):
        return self.office

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email


def test_prob6():
    p1 = Person("Kim", office="1234567", email="kim@company.com")
    p2 = Person("Park", office="2345678")
    p2.setEmail("park@company.com")


if __name__ == "__main__":
    test_prob6()