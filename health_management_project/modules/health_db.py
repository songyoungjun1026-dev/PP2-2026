

# HealthRecord
# HealthManager

import json
import os
import pickle
import csv


# 환자 정보 클래스
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

    # 딕셔너리 변환
    def to_dict(self):
        return {
            "id": self.id,
            "birth": self.birth,
            "gender": self.gender,
            "name": self.name,
            "height": self.height,
            "weight": self.weight,
            "bmi": self.bmi,
            "status": self.status
        }


# 파일 저장 및 불러오기 클래스
class HealthManager:
    def __init__(self):
        self.datas = []

        # AI 사용: 파일 경로 설정
        base_path = os.path.join(os.path.dirname(__file__), "..", "data")

        self.file_path = os.path.join(base_path, "data.json")
        self.csv_path = os.path.join(base_path, "data.csv")
        self.pickle_path = os.path.join(base_path, "data.pickle")
        self.txt_path = os.path.join(base_path, "data.txt")

        # AI 사용: 데이터 폴더 자동 생성
        os.makedirs(base_path, exist_ok=True)

    # JSON 파일 저장
    def update_file(self):
        data = []

        for info in self.datas:
            data.append(info.to_dict())

        try:
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

            print("JSON 파일 저장 완료")

        except OSError:
            print("JSON 파일 저장 실패")

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

            print("JSON 파일 불러오기 완료")

        except FileNotFoundError:
            print("JSON 파일이 없습니다.")

        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            print("JSON 파일이 손상되었습니다.")

    # CSV 파일 저장
    # AI 사용: CSV 파일 저장
    def save_csv(self):
        try:
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

            print("CSV 파일 저장 완료")

        except OSError:
            print("CSV 파일 저장 실패")

    # CSV 파일 불러오기
    # AI 사용: CSV 파일 읽기
    def load_csv(self):
        try:
            with open(self.csv_path, "r", encoding="utf-8-sig") as f:
                reader = csv.DictReader(f)

                data_list = []

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

                    data_list.append(info)

            self.datas = data_list

            print("CSV 파일 불러오기 완료")

        except FileNotFoundError:
            print("CSV 파일이 없습니다.")

        except (KeyError, ValueError, TypeError):
            print("CSV 파일이 손상되었습니다.")

    # PICKLE 파일 저장
    # AI 사용: PICKLE 파일 저장
    def save_pickle(self):
        try:
            with open(self.pickle_path, "wb") as f:
                pickle.dump(self.datas, f)

            print("PICKLE 파일 저장 완료")

        except OSError:
            print("PICKLE 파일 저장 실패")

    # PICKLE 파일 불러오기
    # AI 사용: PICKLE 파일 읽기
    def load_pickle(self):
        try:
            with open(self.pickle_path, "rb") as f:
                data = pickle.load(f)

            if not isinstance(data, list):
                print("PICKLE 파일 형식이 올바르지 않습니다.")
                return

            self.datas = data

            print("PICKLE 파일 불러오기 완료")

        except FileNotFoundError:
            print("PICKLE 파일이 없습니다.")

        except (pickle.UnpicklingError, EOFError, AttributeError):
            print("PICKLE 파일이 손상되었습니다.")

    # TXT 파일 저장
    # AI 사용: TXT 파일 저장
    def save_txt(self):
        try:
            with open(self.txt_path, "w", encoding="utf-8") as f:
                for info in self.datas:
                    f.write(
                        f"{info.id},{info.birth},{info.gender},"
                        f"{info.name},{info.height},{info.weight},"
                        f"{info.bmi},{info.status}\n"
                    )

            print("TXT 파일 저장 완료")

        except OSError:
            print("TXT 파일 저장 실패")

    # TXT 파일 불러오기
    # AI 사용: TXT 파일 읽기
    def load_txt(self):
        try:
            data_list = []

            with open(self.txt_path, "r", encoding="utf-8") as f:
                for line in f:
                    data = line.strip().split(",")

                    if len(data) != 8:
                        raise ValueError

                    info = Healthrecord(
                        data[0],
                        int(data[1]),
                        data[2],
                        data[3],
                        float(data[4]),
                        float(data[5]),
                        float(data[6]),
                        data[7]
                    )

                    data_list.append(info)

            self.datas = data_list

            print("TXT 파일 불러오기 완료")

        except FileNotFoundError:
            print("TXT 파일이 없습니다.")

        except (ValueError, IndexError):
            print("TXT 파일이 손상되었습니다.")
