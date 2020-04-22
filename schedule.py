import gspread
import datetime
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('secret.json', scope)

client = gspread.authorize(creds)
wks = client.open("Fizmat Online 2019-20").worksheet("9D")

def get_cell_value(row, col):
    return wks.cell(row, col).value


weekday = datetime.date.today().weekday() + 1
subjects_row = range(5, 14)


def get_subjects():
    subject = ''
    for i in subjects_row:
        subject += '\n'+(get_cell_value(i, weekday+3))
    return subject

print(get_subjects())
