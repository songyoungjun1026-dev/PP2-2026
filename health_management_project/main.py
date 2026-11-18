
from modules.health_db import HealthManager

manager = HealthManager()

manager.load_file()

while True:
    print("\n===== 건강관리 프로그램 =====")
    print("1. 환자 정보 추가")
    print("2. JSON 파일 저장")
    print("3. CSV 파일 저장")
    print("4. Pickle 파일 저장")
    print("5. 종료")

    menu = input("메뉴를 선택하세요: ")

    if menu == "1":
        manager.add_file()

    elif menu == "2":
        manager.update_file()

    elif menu == "3":
        manager.save_csv()

    elif menu == "4":
        manager.save_pickle()

    elif menu == "5":
        manager.update_file()
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 메뉴입니다. 다시 선택해주세요.")
