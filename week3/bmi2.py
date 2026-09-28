# 문제

#여러 학생들의 키와 몸무게를 리스트로 입력 받아 BMI 리스트를 출력하는 프로그램을 작성하시오.
#함수와 테스트하는 함수를 작성하시오
#BMI 함수는 지난 시간에 작성한 get_bmi 함수를 이용하여 작성하시오.

#
# 여러 학생들의 BMI 계산하기
#

def get_bmi(weight_kg:float, height_cm:float) -> float:
    bmi = weight_kg / (height_cm/100) ** 2
    return bmi


# 여러 학생의 BMI를 계산하는 함수
def get_bmi_list(students):
    bmi_list = []

    for student in students:
        height = student[0]
        weight = student[1]

        bmi = get_bmi(weight, height)
        bmi_list.append(bmi)

    return bmi_list


# 테스트하는 함수
def test_get_bmi_list():
    students = [
        [165, 58],
        [170, 65],
        [175, 70],
        [160, 50]
    ]

    result = get_bmi_list(students)

    print("학생들의 BMI 리스트")
    print(result)


if __name__ == "__main__":
    test_get_bmi_list()
