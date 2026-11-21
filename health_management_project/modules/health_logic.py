# health_logic.py
# 모듈 2: 비즈니스 로직 (등록 / 조회 / 수정 / 삭제 / 통계)

from modules.health_db import Healthrecord, HealthManager


class HealthLogic:
    def __init__(self):
        self.manager = HealthManager()
        self.file_format = "json"  # 저장 형식: json, csv, pickle, txt

    # ---------------------------------------------------------
    # 파일 저장 / 불러오기 (모듈 1 함수를 그대로 호출)
    # ---------------------------------------------------------
    def set_format(self, fmt):
        self.file_format = fmt

    def save(self):
        if self.file_format == "json":
            self.manager.update_file()
        elif self.file_format == "csv":
            self.manager.save_csv()
        elif self.file_format == "pickle":
            self.manager.save_pickle()
        elif self.file_format == "txt":
            self.manager.save_txt()

    def load(self):
        if self.file_format == "json":
            self.manager.load_file()
        elif self.file_format == "csv":
            self.manager.load_csv()
        elif self.file_format == "pickle":
            self.manager.load_pickle()
        elif self.file_format == "txt":
            self.manager.load_txt()

    # ---------------------------------------------------------
    # BMI, 비만도 계산
    # ---------------------------------------------------------
    def calc_bmi(self, height, weight):
        # BMI = 몸무게 / (키(m) x 키(m))
        meter = height / 100
        return round(weight / (meter * meter), 2)

    def get_status(self, bmi):
        if bmi < 18.5:
            return "저체중"
        elif bmi < 23:
            return "정상"
        elif bmi < 25:
            return "과체중"
        elif bmi < 30:
            return "1단계 비만"
        elif bmi < 35:
            return "2단계 비만"
        else:
            return "3단계 비만"

    # ---------------------------------------------------------
    # 식별번호 자동 생성 (P0001, P0002, ...)
    # ---------------------------------------------------------
    # AI 사용: 가장 큰 번호를 찾아서 +1 하는 방식
    # (중간에 삭제해도 번호가 겹치지 않게 하기 위함)
    def make_id(self):
        max_num = 0

        for info in self.manager.datas:
            num = int(info.id[1:])  # "P0003" -> 3
            if num > max_num:
                max_num = num

        return "P" + str(max_num + 1).zfill(4)  # 4자리로 맞추기

    # ---------------------------------------------------------
    # 신규 등록
    # ---------------------------------------------------------
    def add_record(self, birth, gender, name, height, weight, save=True):
        # 이름 확인
        name = str(name).strip()
        if name == "":
            return False, "이름을 입력하세요."

        # TXT 파일은 쉼표로 구분하기 때문에 이름에 쉼표가 있으면 안 됨
        if "," in name:
            return False, "이름에 쉼표(,)를 쓸 수 없습니다."

        # 성별 확인
        if gender not in ("남", "여"):
            return False, "성별은 '남' 또는 '여'로 입력하세요."

        # 숫자 변환 (글자가 들어오면 오류 처리)
        try:
            birth = int(birth)
            height = float(height)
            weight = float(weight)
        except ValueError:
            return False, "생년, 키, 몸무게는 숫자로 입력하세요."

        if height <= 0 or weight <= 0:
            return False, "키와 몸무게는 0보다 커야 합니다."

        # 중복 확인: 이름, 생년, 성별이 모두 같으면 중복
        for info in self.manager.datas:
            if info.name == name and info.birth == birth and info.gender == gender:
                return False, "이미 등록된 사람입니다."

        # 레코드 만들기
        bmi = self.calc_bmi(height, weight)
        status = self.get_status(bmi)
        new_id = self.make_id()

        info = Healthrecord(new_id, birth, gender, name, height, weight, bmi, status)
        self.manager.datas.append(info)

        if save:
            self.save()

        return True, f"등록 완료 (식별번호: {new_id})"

    # ---------------------------------------------------------
    # 엑셀 파일로 한꺼번에 등록
    # 엑셀 형식: 1행은 제목, 2행부터 [생년, 성별, 이름, 키, 몸무게]
    # ---------------------------------------------------------
    # AI 사용: openpyxl로 엑셀 파일 읽기
    # (설치 필요: pip install openpyxl)
    def add_from_excel(self, path):
        try:
            from openpyxl import load_workbook

            wb = load_workbook(path)
            ws = wb.active
        except ImportError:
            return False, "openpyxl이 설치되지 않았습니다."
        except FileNotFoundError:
            return False, "엑셀 파일이 없습니다."
        except Exception:
            return False, "엑셀 파일을 읽을 수 없습니다."

        success = 0
        fail = 0

        # min_row=2 : 제목 줄은 건너뛰기
        for row in ws.iter_rows(min_row=2, values_only=True):
            birth, gender, name, height, weight = row[:5]

            ok, msg = self.add_record(birth, gender, name, height, weight, save=False)

            if ok:
                success += 1
            else:
                fail += 1

        # 마지막에 한 번만 저장
        if success > 0:
            self.save()

        return True, f"성공 {success}건, 실패(중복 포함) {fail}건"

    # ---------------------------------------------------------
    # 조회 / 검색
    # ---------------------------------------------------------
    def get_all(self):
        return self.manager.datas

    def find_by_id(self, record_id):
        for info in self.manager.datas:
            if info.id == record_id:
                return info
        return None

    # 이름 또는 식별번호에 검색어가 들어있으면 결과에 추가
    def search(self, keyword):
        keyword = keyword.strip()
        result = []

        for info in self.manager.datas:
            if keyword in info.name or keyword in info.id:
                result.append(info)

        return result

    # ---------------------------------------------------------
    # 수정 (키, 몸무게를 바꾸면 BMI와 비만도도 다시 계산)
    # ---------------------------------------------------------
    def update_record(self, record_id, height, weight):
        info = self.find_by_id(record_id)

        if info is None:
            return False, "해당 식별번호가 없습니다."

        try:
            height = float(height)
            weight = float(weight)
        except ValueError:
            return False, "키와 몸무게는 숫자로 입력하세요."

        if height <= 0 or weight <= 0:
            return False, "키와 몸무게는 0보다 커야 합니다."

        info.height = height
        info.weight = weight
        info.bmi = self.calc_bmi(height, weight)
        info.status = self.get_status(info.bmi)

        self.save()
        return True, f"수정 완료 (BMI {info.bmi}, {info.status})"

    # ---------------------------------------------------------
    # 삭제
    # ---------------------------------------------------------
    def delete_record(self, record_id):
        info = self.find_by_id(record_id)

        if info is None:
            return False, "해당 식별번호가 없습니다."

        self.manager.datas.remove(info)
        self.save()
        return True, "삭제 완료"

    # ---------------------------------------------------------
    # 통계 (인원수, 평균 키, 평균 몸무게, 평균 BMI)
    # ---------------------------------------------------------
    def get_statistics(self):
        count = len(self.manager.datas)

        # 데이터가 없으면 0으로 나누기 오류가 나므로 먼저 처리
        if count == 0:
            return {"count": 0, "avg_height": 0, "avg_weight": 0, "avg_bmi": 0}

        total_height = 0
        total_weight = 0
        total_bmi = 0

        for info in self.manager.datas:
            total_height += info.height
            total_weight += info.weight
            total_bmi += info.bmi

        return {
            "count": count,
            "avg_height": round(total_height / count, 2),
            "avg_weight": round(total_weight / count, 2),
            "avg_bmi": round(total_bmi / count, 2),
        }