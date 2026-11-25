import tkinter as tk
from modules.health_gui import HealthGUI

root = tk.Tk()
root.title("건강관리 프로그램")
root.geometry("1000x650")

app = HealthGUI(root)

root.mainloop()