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

def get_schedule(grade):
    lsch = wks.worksheet(grade)
    subject = []
    for i in subjects_col:
        subject.append(lsch.cell(i, weekday + 3).value)
    write_json(subject, grade)
    return subject

def get_all_titles():
    titles_list = str(wks.worksheets())
    clear_titles = re.findall(r"[']+\w+", titles_list)
    clear_titles = list(map(lambda x: x[1:], clear_titles))
    write_json(clear_titles, "Clases")

def get_all_schedule():
    grades = read_json("Clases")
    for i in grades:
        get_schedule(i)
        time.sleep(10)




def write_json(data, grade):
    with open('schedule_cache/schedule_'+grade+'.json', 'w') as outfile:
        json.dump(data, outfile, indent=2, ensure_ascii=False)

def read_json(grade):
    with open('schedule_cache/schedule_'+grade+'.json') as outfile:
        data = json.load(outfile)
        return data