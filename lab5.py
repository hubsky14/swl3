import requests
from datetime import date


def send_request_and_save_result(url):
    a = requests.get(url)
    today = date.today()

    with open("zapytanie.txt", "a") as file:
        file.write('Wysłano zapytanie do : ' + url + '\n')
        file.write('Data: ' + str(today) + '\n \n')
        file.write('Zawartosc: ' + str(a.content) '\n \n')

send_request_and_save_result("http://kcir.pwr.edu.pl")
