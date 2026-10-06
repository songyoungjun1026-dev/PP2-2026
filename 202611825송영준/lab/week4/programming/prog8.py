# 작성자: 송영준
# 작성일: 2026-10-03
# 문제: printSong이라는 클래스를 작성해보자.
#       printSong의 생성자는 노래의 가사를 리스트 형태로 받아서 객체의 내부에 저장.
#       sing() 메소드는 한 줄에 한 항목씩 출력한다.
# 클래스: printSong
# 인스턴스 변수: Song (가사 문자열을 담은 리스트)
# 생성자: 전달받은 가사 리스트를 객체의 속성에 저장한다.
# sing: 각 가사 항목을 출력한다.


class printSong:
    def __init__(self, Song):
        self.Song = Song

    def sing(self):
        for line in self.Song:
            print(line)

def test_prob8():
    aSong = printSong(["TWINKLE, twinkle, little star",
                    "How I wonder what you are!",
                    "Up above the world so high,",
                    "Like a diamond in the sky."])
    aSong.sing()

if __name__ == "__main__":
    test_prob8()