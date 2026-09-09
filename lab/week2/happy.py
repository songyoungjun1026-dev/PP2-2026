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

   