def get_BMI(height, weight):
    return weight / ((height / 100) ** 2)


def get_BMI_list(heights: list[float], weights: list[float]) -> list[float]:
    bmi_list = []

    for height, weight in zip(heights, weights):
        bmi = get_BMI(height, weight)
        bmi_list.append(bmi)

    return bmi_list


def test_get_BMI_list():
    heights = [170, 160, 180]
    weights = [65, 50, 80]

    result = get_BMI_list(heights, weights)

    print("키:", heights)
    print("몸무게:", weights)
    print("BMI:", result)


test_get_BMI_list()
