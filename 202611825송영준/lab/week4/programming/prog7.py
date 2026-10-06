# 작성자: 송영준
# 작성일: 2026-10-03
# 문제: 사람들의 연락처를 저장하는 PhoneBook 클래스를 작성해보자.
# 클래스: PhoneBook
# 인스턴스 변수: contacts (연락처를 저장하는 딕셔너리)
# 휴대폰 번호, 직장 전화번호, 이메일은 None 기본값을 가진다.
# 생성자: 객체마다 빈 연락처 딕셔너리를 생성한다.
# __str__: None이 아닌 항목만 문자열로 만들고 줄바꿈으로 연결한다.


class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def __str__(self):
            lines = []
            for name, info in self.contacts.items():
                if lines:
                    lines.append("")
                lines.append(name)
                if info["mobile"] is not None:
                    lines.append(f"mobile phone: {info['mobile']}")
                if info["office"] is not None:
                    lines.append(f"office phone: {info['office']}")
                if info["email"] is not None:
                    lines.append(f"email address: {info['email']}")
            return "\n".join(lines)

    def add(self, name, mobile=None, office=None, email=None):
        self.contacts[name] = {
            "mobile": mobile,
            "office": office,
            "email": email,
        }

def test_prob7():
    obj = PhoneBook()
    obj.add("Kim", office="1234567", email="kim@company.com")
    obj.add("Park", office="2345678", email="park@company.com")
    print(obj)

if __name__ == "__main__":
    test_prob7()

