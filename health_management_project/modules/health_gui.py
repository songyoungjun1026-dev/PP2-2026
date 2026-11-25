
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from modules.health_logic import HealthLogic


class HealthGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("건강관리 프로그램")
        self.root.geometry("1000x650")
        self.root.minsize(850, 550)

        self.logic = HealthLogic()
        self.logic.load()
        self.selected_id = None

        # AI 사용: 전체 화면을 입력, 버튼, 표 영역으로 구분
        main = ttk.Frame(root, padding=15)
        main.pack(fill="both", expand=True)

        # 입력창
        input_frame = ttk.LabelFrame(
            main, text="환자 정보 입력", padding=10
        )
        input_frame.pack(fill="x", pady=5)

        self.entries = {}
        fields = ["생년", "성별", "이름", "키", "몸무게"]

        for i, field in enumerate(fields):
            ttk.Label(input_frame, text=field).grid(
                row=0, column=i, padx=10, pady=5
            )

            if field == "성별":
                entry = ttk.Combobox(
                    input_frame,
                    values=["남", "여"],
                    state="readonly",
                    width=15
                )
            else:
                entry = ttk.Entry(input_frame, width=18)

            entry.grid(row=1, column=i, padx=10, pady=5)
            self.entries[field] = entry

        # AI 사용: 등록 및 관리 버튼을 한 줄로 배치
        button_frame = ttk.Frame(main)
        button_frame.pack(fill="x", pady=10)

        buttons = [
            ("등록", self.add),
            ("수정", self.update),
            ("삭제", self.delete),
            ("초기화", self.clear),
            ("전체조회", self.show_all)
        ]

        for name, command in buttons:
            ttk.Button(
                button_frame,
                text=name,
                command=command
            ).pack(side="left", padx=5)

        # 검색 및 파일 관리
        file_frame = ttk.LabelFrame(
            main, text="검색 및 파일 관리", padding=10
        )
        file_frame.pack(fill="x", pady=5)

        self.search_entry = ttk.Entry(file_frame, width=25)
        self.search_entry.pack(side="left", padx=5)

        ttk.Button(
            file_frame, text="검색", command=self.search
        ).pack(side="left", padx=5)

        self.fmt = tk.StringVar(value="json")

        ttk.Combobox(
            file_frame,
            textvariable=self.fmt,
            values=["json", "csv", "pickle", "txt"],
            state="readonly",
            width=12
        ).pack(side="left", padx=15)

        ttk.Button(
            file_frame, text="저장", command=self.save
        ).pack(side="left", padx=5)

        ttk.Button(
            file_frame, text="불러오기", command=self.load
        ).pack(side="left", padx=5)

        ttk.Button(
            file_frame, text="엑셀 등록", command=self.excel
        ).pack(side="left", padx=5)

        ttk.Button(
            file_frame, text="통계", command=self.statistics
        ).pack(side="left", padx=5)

        # AI 사용: 환자 정보를 표시하는 표 생성
        table_frame = ttk.LabelFrame(
            main, text="환자 정보 목록", padding=5
        )
        table_frame.pack(fill="both", expand=True, pady=10)

        columns = (
            "id", "birth", "gender", "name",
            "height", "weight", "bmi", "status"
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        names = [
            "식별번호", "생년", "성별", "이름",
            "키", "몸무게", "BMI", "비만도"
        ]

        for col, name in zip(columns, names):
            self.tree.heading(col, text=name)
            self.tree.column(col, width=100, anchor="center")

        # AI 사용: 가로 및 세로 스크롤바
        y_scroll = ttk.Scrollbar(
            table_frame, orient="vertical",
            command=self.tree.yview
        )

        x_scroll = ttk.Scrollbar(
            table_frame, orient="horizontal",
            command=self.tree.xview
        )

        self.tree.configure(
            yscrollcommand=y_scroll.set,
            xscrollcommand=x_scroll.set
        )

        self.tree.grid(row=0, column=0, sticky="nsew")
        y_scroll.grid(row=0, column=1, sticky="ns")
        x_scroll.grid(row=1, column=0, sticky="ew")

        table_frame.rowconfigure(0, weight=1)
        table_frame.columnconfigure(0, weight=1)

        self.tree.bind("<<TreeviewSelect>>", self.select)

        self.show_all()

    # 입력값 가져오기
    def get_values(self):
        return [
            self.entries[x].get()
            for x in ["생년", "성별", "이름", "키", "몸무게"]
        ]

    # 입력창 비우기
    def clear(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

        self.selected_id = None
        self.tree.selection_remove(self.tree.selection())

    # AI 사용: 환자 목록 표에 데이터 출력
    def show_all(self):
        self.tree.delete(*self.tree.get_children())

        for x in self.logic.get_all():
            self.tree.insert("", "end", values=(
                x.id, x.birth, x.gender, x.name,
                x.height, x.weight, x.bmi, x.status
            ))

    # 환자 등록
    def add(self):
        try:
            person = self.logic.add_record(*self.get_values())

            messagebox.showinfo(
                "등록 완료",
                f"{person.name} 환자 등록 완료!\nID: {person.id}"
            )

            self.show_all()
            self.clear()

        except ValueError as e:
            messagebox.showerror("등록 오류", str(e))

    # 환자 선택
    def select(self, event):
        selected = self.tree.selection()

        if not selected:
            return

        values = self.tree.item(selected[0], "values")
        self.selected_id = values[0]

        for key, value in zip(self.entries, values[1:6]):
            self.entries[key].delete(0, tk.END)
            self.entries[key].insert(0, value)

    # 환자 정보 수정
    def update(self):
        if not self.selected_id:
            messagebox.showwarning("오류", "환자를 선택하세요.")
            return

        try:
            result = self.logic.update_record(
                self.selected_id,
                self.entries["키"].get(),
                self.entries["몸무게"].get()
            )

            if result:
                messagebox.showinfo("수정", "수정 완료")
                self.show_all()
                self.clear()
            else:
                messagebox.showerror("오류", "환자를 찾을 수 없습니다.")

        except ValueError as e:
            messagebox.showerror("수정 오류", str(e))

    # 환자 삭제
    def delete(self):
        if not self.selected_id:
            messagebox.showwarning("오류", "환자를 선택하세요.")
            return

        if messagebox.askyesno("삭제", "삭제하시겠습니까?"):
            result = self.logic.delete_record(self.selected_id)

            if result:
                messagebox.showinfo("삭제", "삭제 완료")
                self.show_all()
                self.clear()
            else:
                messagebox.showerror("오류", "환자를 찾을 수 없습니다.")

    # 환자 검색
    def search(self):
        keyword = self.search_entry.get()

        result = self.logic.search(keyword)

        self.tree.delete(*self.tree.get_children())

        for x in result:
            self.tree.insert("", "end", values=(
                x.id, x.birth, x.gender, x.name,
                x.height, x.weight, x.bmi, x.status
            ))

    # 데이터 저장
    def save(self):
        self.logic.set_format(self.fmt.get())
        self.logic.save()

        messagebox.showinfo("저장", "저장 요청 완료")

    # 데이터 불러오기
    def load(self):
        self.logic.set_format(self.fmt.get())
        self.logic.load()

        self.show_all()
        self.clear()

        messagebox.showinfo("불러오기", "불러오기 완료")

    # 엑셀 등록
    def excel(self):
        path = filedialog.askopenfilename(
            filetypes=[("Excel 파일", "*.xlsx")]
        )

        if path:
            try:
                count = self.logic.add_from_excel(path)

                self.show_all()

                messagebox.showinfo(
                    "엑셀 등록",
                    f"{count}명의 환자를 등록했습니다."
                )

            except Exception as e:
                messagebox.showerror("엑셀 오류", str(e))

    # 통계
    def statistics(self):
        s = self.logic.get_statistics()

        messagebox.showinfo(
            "통계",
            f"전체 인원: {s['count']}명\n"
            f"평균 키: {s['avg_height']}cm\n"
            f"평균 몸무게: {s['avg_weight']}kg\n"
            f"평균 BMI: {s['avg_bmi']}"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = HealthGUI(root)
    root.mainloop()
