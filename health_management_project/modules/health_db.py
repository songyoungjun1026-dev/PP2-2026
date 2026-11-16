
# HealthRecord
# HealthManager

import json
import os
import pickle
import csv

class Healthrecord:
    def __init__(self, id, birth, gender, name, height, weight, bmi, status):
        self.id = id
        self.birth = birth
        self.gender = gender
        self.name = name
        self.height = height
        self.weight = weight
        self.bmi = bmi
        self.status = status

    def get_bmi(self):
        bmi = self.weight / ((self.height / 100) ** 2)
        return round(bmi, 1)


class HealthManager:
    def __init__(self):
        self.datas = []

        # AI는 사용하지 않았으나 파일 입출력 강의 PPT 참고
        self.file_path = os.path.join(
            os.path.dirname(__file__), "..", "data", "data.json"
        )

        try:
            if not os.path.exists(self.file_path):
                raise FileNotFoundError

        except FileNotFoundError:
            print("존재하지 않는 파일입니다. 경로를 다시 확인해주세요.")

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

    # 파일 불러오기
    def load_file(self):
        # AI 사용: JSON 파일 읽기
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
                last_id = self.datas[-1].id
                self.last_id = int(last_id.split("-")[1])

        except FileNotFoundError:
            print("파일이 존재하지 않습니다.")

    # 파일 저장하기
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

        print("파일 저장이 완료되었습니다.")
