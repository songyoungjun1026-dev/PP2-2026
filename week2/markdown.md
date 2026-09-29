# 리스트 타입힌트 연습

names: list[str] = ["영준", "정아", "민재", "완도"]

print("학생 목록:", names)

def print_names(names: list[str]) -> None:
    for name in names:
        print("학생 이름:", name)

print_names(names)

def count_students(names: list[str]) -> int:
    return len(names)

print("학생 수:", count_students(names))
