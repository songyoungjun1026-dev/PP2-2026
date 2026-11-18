


# HealthRecord
# HealthManager

import json
import os
import pickle
import csv


class Healthrecord:
    def __init__(self, birth, gender, name, height, weight, bmi):
        self.birth = birth
        self.gender = gender
        self.name = name
        self.height = height
        self.weight = weight
        self.bmi = bmi


class HealthManager:
    def __init__(self):
        self.datas = []

        # AI 사용: JSON, CSV, PICKLE 파일 경로 설정
        base_path = os.path.join(os.path.dirname(__file__), "..", "data")

        self.file_path = os.path.join(base_path, "data.json")
        self.csv_path = os.path.join(base_path, "data.csv")
        self.pickle_path = os.path.join(base_path, "data.pickle")

        # AI 사용: 데이터 폴더가 없으면 자동 생성
        os.makedirs(base_path, exist_ok=True)

        # AI 사용: 마지막 환자 번호 저장
        self.last_id = 0

    # AI 사용: 환자식별번호 자동 생성
    def random_id(self):
        self.last_id += 1
        return f"P2026-{self.last_id:04d}"

    # 환자 정보 추가
    def add_file(self):
        id = self.random_id()

        name = input("이름을 입력하세요: ")
        birth = int(input("태어난 연도를 입력하세요: "))
        gender = input("성별을 입력하세요(남/여): ")
        height = float(input("키를 입력하세요: "))
        weight = float(input("몸무게를 입력하세요: "))

        temp = Healthrecord(id, birth, gender, name, height, weight, 0, "")

        bmi = temp.get_bmi()

        status = (
            "저체중" if bmi < 18.5 else
            "정상" if bmi < 23 else
            "과체중" if bmi < 25 else
            "비만" if bmi < 30 else
            "고도비만"
        )

        user_info = Healthrecord(
            id, birth, gender, name, height, weight, bmi, status
        )

        self.datas.append(user_info)

        print("환자 정보가 추가되었습니다.")
        print("환자식별번호:", id)

    # JSON 파일 불러오기
    # AI 사용: JSON 파일 읽기
    def load_file(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.datas = []

            for item in data:
                info = Healthrecord(
                    item["id"],
                    item["birth"],
                    item["gender"],
                    item["name"],
                    item["height"],
                    item["weight"],
                    item["bmi"],
                    item["status"]
                )

                self.datas.append(info)

            # AI 사용: 마지막 환자 번호 확인
            if self.datas:
                self.last_id = max(
                    int(info.id.split("-")[1]) for info in self.datas
                )

        except FileNotFoundError:
            print("JSON 파일이 존재하지 않습니다.")

    # JSON 파일 저장하기
    def update_file(self):
        data = []

        for info in self.datas:
            data.append({
                "id": info.id,
                "birth": info.birth,
                "gender": info.gender,
                "name": info.name,
                "height": info.height,
                "weight": info.weight,
                "bmi": info.bmi,
                "status": info.status
            })

        # JSON 파일에 저장
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print("JSON 파일 저장이 완료되었습니다.")

    # AI 사용: CSV 파일 불러오기
    def load_csv(self):
        try:
            with open(self.csv_path, "r", encoding="utf-8-sig") as f:
                reader = csv.DictReader(f)

                self.datas = []

                for item in reader:
                    info = Healthrecord(
                        item["id"],
                        int(item["birth"]),
                        item["gender"],
                        item["name"],
                        float(item["height"]),
                        float(item["weight"]),
                        float(item["bmi"]),
                        item["status"]
                    )

                    self.datas.append(info)

            if self.datas:
                self.last_id = max(
                    int(info.id.split("-")[1]) for info in self.datas
                )

            print("CSV 파일 불러오기가 완료되었습니다.")

        except FileNotFoundError:
            print("CSV 파일이 존재하지 않습니다.")

    # AI 사용: CSV 파일 저장하기
    def save_csv(self):
        with open(self.csv_path, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)

            writer.writerow([
                "id", "birth", "gender", "name",
                "height", "weight", "bmi", "status"
            ])

            for info in self.datas:
                writer.writerow([
                    info.id,
                    info.birth,
                    info.gender,
                    info.name,
                    info.height,
                    info.weight,
                    info.bmi,
                    info.status
                ])

        print("CSV 파일 저장이 완료되었습니다.")

    # AI 사용: PICKLE 파일 불러오기
    def load_pickle(self):
        try:
            with open(self.pickle_path, "rb") as f:
                self.datas = pickle.load(f)

            if self.datas:
                self.last_id = max(
                    int(info.id.split("-")[1]) for info in self.datas
                )

            print("PICKLE 파일 불러오기가 완료되었습니다.")

        except FileNotFoundError:
            print("PICKLE 파일이 존재하지 않습니다.")

    # AI 사용: PICKLE 파일 저장하기
    def save_pickle(self):
        with open(self.pickle_path, "wb") as f:
            pickle.dump(self.datas, f)

        print("PICKLE 파일 저장이 완료되었습니다.")
