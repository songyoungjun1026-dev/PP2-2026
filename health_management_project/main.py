from modules.health_logic import HealthLogic

logic = HealthLogic()
logic.load()

while True:
    print("\n===== 건강관리 프로그램 =====")
    print("1. 환자 정보 추가")
    print("2. JSON 파일 저장")
    print("3. CSV 파일 저장")
    print("4. Pickle 파일 저장")
    print("5. TXT 파일 저장")
    print("6. 종료")

    menu = input("메뉴를 선택하세요: ")

    if menu == "1":
        birth = input("생년: ")
        gender = input("성별 (남/여): ")
        name = input("이름: ")
        height = input("키(cm): ")
        weight = input("몸무게(kg): ")

        ok, msg = logic.add_record(
            birth, gender, name, height, weight
        )
        print(msg)

    elif menu == "2":
        logic.set_format("json")
        logic.save()

    elif menu == "3":
        logic.set_format("csv")
        logic.save()

    elif menu == "4":
        logic.set_format("pickle")
        logic.save()

    elif menu == "5":
        logic.set_format("txt")
        logic.save()

    elif menu == "6":
        logic.set_format("json")
        logic.save()
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 메뉴입니다. 다시 선택해주세요.")