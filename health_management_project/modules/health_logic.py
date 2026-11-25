
from modules.health_db import Healthrecord, HealthManager


class HealthLogic:
    def __init__(self):
        self.manager = HealthManager()
        self.file_format = "json"

    # AI 사용: 저장 형식에 따라 파일 저장
    def set_format(self, file_format):
        self.file_format = file_format

    # AI 사용: 선택한 형식으로 데이터 저장
    def save(self):
        if self.file_format == "json":
            self.manager.update_file()
        elif self.file_format == "csv":
            self.manager.save_csv()
        elif self.file_format == "pickle":
            self.manager.save_pickle()
        elif self.file_format == "txt":
            self.manager.save_txt()

    # AI 사용: 선택한 형식의 데이터 불러오기
    def load(self):
        if self.file_format == "json":
            self.manager.load_file()
        elif self.file_format == "csv":
            self.manager.load_csv()
        elif self.file_format == "pickle":
            self.manager.load_pickle()
        elif self.file_format == "txt":
            self.manager.load_txt()

    # AI 사용: BMI 계산
    def calc_bmi(self, height, weight):
        height = float(height) / 100
        weight = float(weight)
        return round(weight / (height * height), 2)

    # AI 사용: BMI에 따른 건강 상태 판정
    def get_status(self, bmi):
        if bmi < 18.5:
            return "저체중"
        elif bmi < 23:
            return "정상"
        elif bmi < 25:
            return "과체중"
        else:
            return "비만"

    # AI 사용: 기존 환자 ID를 확인하고 다음 ID 생성
    def make_id(self):
        numbers = []

        for person in self.manager.datas:
            try:
                numbers.append(int(person.id[1:]))
            except:
                pass

        if numbers:
            return "P" + str(max(numbers) + 1).zfill(4)

        return "P0001"

    # AI 사용: 환자 정보 등록
    def add_record(self, birth, gender, name, height, weight, save=True):
        if not all([birth, gender, name, height, weight]):
            raise ValueError("모든 정보를 입력하세요.")

        height = float(height)
        weight = float(weight)

        if height <= 0 or weight <= 0:
            raise ValueError("키와 몸무게는 0보다 커야 합니다.")

        # AI 사용: 생년월일과 이름이 같은 환자 중복 등록 방지
        for person in self.manager.datas:
            if person.name == name and person.birth == birth:
                raise ValueError("이미 등록된 환자입니다.")

        bmi = self.calc_bmi(height, weight)
        status = self.get_status(bmi)

        person = Healthrecord(
            self.make_id(), birth, gender, name,
            height, weight, bmi, status
        )

        self.manager.datas.append(person)

        if save:
            self.save()

        return person

    # 전체 환자 조회
    def get_all(self):
        return self.manager.datas

    # ID로 환자 검색
    def find_by_id(self, person_id):
        for person in self.manager.datas:
            if person.id == person_id:
                return person
        return None

    # AI 사용: 이름 또는 ID로 환자 검색
    def search(self, keyword):
        result = []

        for person in self.manager.datas:
            if (keyword.lower() in person.name.lower()
                    or keyword.lower() in person.id.lower()):
                result.append(person)

        return result

    # AI 사용: 환자 정보 수정 및 BMI 재계산
    def update_record(self, person_id, height, weight):
        person = self.find_by_id(person_id)

        if person is None:
            return False

        height = float(height)
        weight = float(weight)

        if height <= 0 or weight <= 0:
            raise ValueError("키와 몸무게는 0보다 커야 합니다.")

        person.height = height
        person.weight = weight
        person.bmi = self.calc_bmi(height, weight)
        person.status = self.get_status(person.bmi)

        self.save()
        return True

    # 환자 정보 삭제
    def delete_record(self, person_id):
        person = self.find_by_id(person_id)

        if person is None:
            return False

        self.manager.datas.remove(person)
        self.save()
        return True

    # AI 사용: 엑셀 파일에서 환자 정보 가져오기
    def add_from_excel(self, path):
        import openpyxl

        workbook = openpyxl.load_workbook(path)
        sheet = workbook.active

        count = 0

        for row in sheet.iter_rows(min_row=2, values_only=True):
            if not all(row[:5]):
                continue

            try:
                self.add_record(
                    str(row[0]), str(row[1]), str(row[2]),
                    row[3], row[4], save=False
                )
                count += 1
            except ValueError:
                continue

        self.save()
        workbook.close()

        return count

    # AI 사용: 전체 환자 통계 계산
    def get_statistics(self):
        datas = self.manager.datas

        if not datas:
            return {
                "count": 0,
                "avg_height": 0,
                "avg_weight": 0,
                "avg_bmi": 0
            }

        count = len(datas)

        return {
            "count": count,
            "avg_height": round(sum(p.height for p in datas) / count, 2),
            "avg_weight": round(sum(p.weight for p in datas) / count, 2),
            "avg_bmi": round(sum(p.bmi for p in datas) / count, 2)
        }
