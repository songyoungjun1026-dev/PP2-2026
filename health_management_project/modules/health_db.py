# HealthRecord
# HealthManager

import json
import csv
import pickle
import none

class Healthrecord:
    def __init__(self,id,name,birth_year,gender,height,weight,bmi,status):
        self.id = id
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self.height = height
        self.weight = weight
        self.bmi = round(weight / (height / 100)**2,2)
        self.status = (
            "저체중" if self.bmi < 18.5 else
            "정상" if self.bmi < 23 else
            "과체중" if self.bmi < 25 else
            "비만" if self.bmi < 30 else "고도비만"
        )



class HealthManager:
    def __init__

