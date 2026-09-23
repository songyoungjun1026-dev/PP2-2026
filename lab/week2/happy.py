#
#
# 생일 축하 함수
def happy_birthday(name) :
    print("안녕하세요, " + str(name) + "님!")
    return None


def test_happy_birthday2() :
    names = ["윤완", "영준", "민재", "정아"]
    for name in names:
        happy_birthday(name)

def test_happy_birthday3() :
    happy_birthday(3.14159)
    happy_birthday(100)
    happy_birthday([1,2,3 , 4, 5])

if __name__ == "__main__":
    test_happy_birthday2()
    test_happy_birthday3()

   #
# 자기소개 함수
#
def introduce(name, age):
    print("안녕하세요. 저는 " + str(name) + "입니다.")
    print("나이는 " + str(age) + "살입니다.")
    return None


def test_introduce():
    introduce("윤완", 20)
    introduce("영준", 20)
    introduce("민재", 20)


if __name__ == "__main__":
    test_introduce()