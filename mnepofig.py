from oauth2client.service_account import ServiceAccountCredentials
import datetime
import gspread
import re
import json
import time
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('secret.json', scope)

client = gspread.authorize(creds)

weekday = datetime.date.today().weekday() + 1

subjects_col = range(5, 15)

wks = client.open("Fizmat Online 2019-20")

def get_day_schedule(grade): #Получает расписание на день
    lsch = wks.worksheet(grade)
    subject = []
    for i in subjects_col:
        subject.append(lsch.cell(i, weekday + 3).value)
    write_json(subject, grade)
    return subject

def get_all_titles(): #Получает литеру классов
    titles_list = str(wks.worksheets())
    clear_titles = re.findall(r"[']+\w+", titles_list)
    clear_titles = list(map(lambda x: x[1:], clear_titles))
    write_json(clear_titles, "clases")

def get_all_schedule(): #Получает все расписание
    grades = read_json("clases")
    for i in grades:
        get_week_schedule(i)
        time.sleep(10)

def get_time_schedule(): #Получает время
    lsch = wks.sheet1
    subject = []
    for i in subjects_col:
        subject.append(lsch.cell(i, 3).value)
    write_json(subject, "time")
    return subject

def get_week_schedule(grade): #Получает расписание на неделю
    lsch = wks.worksheet(grade)
    k = lsch.get_all_values()
    k = list(map(lambda x: x[3:], k))
    del k[0:4]
    k = list(map(list, zip(*k)))
    write_json(k, grade)
    return k


def write_json(data, grade):
    with open('schedule_cache/schedule_'+grade+'.json', 'w') as outfile:
        json.dump(data, outfile, indent=2, ensure_ascii=False)

def read_json(grade):
    with open('schedule_cache/schedule_'+grade+'.json') as outfile:
        data = json.load(outfile)
        return data