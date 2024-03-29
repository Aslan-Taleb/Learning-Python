import os
import requests
from datetime import datetime

# ENVIRONMENT VARIABLES
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
TOKEN_SHEETY = os.environ["TOKEN_SHEETY"]
GENDER = "male"
WEIGHT_KG = 80
AGE = 21
HEIGHT_CM = 176
LINK_EXERCICE = "https://trackapi.nutritionix.com/v2/natural/exercise"
end_point_row = "https://api.sheety.co/52e4797d4ba4a030a600379c091918dd/myWorkouts/workouts"


def get_user_info():
    while True:
        weight = float(input("Quel est votre poids en kilogrammes ? "))
        if 30 <= weight <= 300:
            break
        else:
            print("Veuillez entrer un poids valide entre 30 et 300 kg.")

    while True:
        height = float(input("Quelle est votre taille en centimètres ? "))
        if 60 <= height <= 250:
            break
        else:
            print("Veuillez entrer une taille valide entre 60 et 250 cm.")

    while True:
        age = int(input("Quel est votre âge ? "))
        if 8 <= age <= 120:
            break
        else:
            print("Veuillez entrer un âge valide entre 8 et 120 ans.")

    return weight, height, age


def get_exercice():
    exercise_text = input("Dites-moi quels exercices vous avez faits : ")
    header = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
    }
    param = {
        'query': exercise_text,
        "gender": GENDER,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE
    }
    response = requests.post(LINK_EXERCICE, json=param, headers=header)
    response = response.json()
    return response


def add_row(exercise_name, exercise_duration, exercise_calories):
    headers = {
        "Authorization": f"Bearer {TOKEN_SHEETY}",
        "Content-Type": "application/json",
        "cache-control": "no-cache"
    }
    today_date = datetime.now().strftime("%d/%m/%Y")
    now_time = datetime.now().strftime("%X")
    inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise_name,
            "duration": exercise_duration,
            "calories": exercise_calories
        }
    }
    requests.post(end_point_row, json=inputs, headers=headers)
    print("L'exercice a été enregistré avec succès !")
