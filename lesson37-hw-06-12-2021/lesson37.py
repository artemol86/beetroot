'''
З використанням будь-яких зручних інструментів, створити програму, яка дозволяє планувати робочий час спеціалістів (наприклад, лікарів). 
Програма має зберігати інформацію про робочі дні спеціаліста протягом наступного тижня - кожен день може бути робочим чи вихідним, у робочі дні спеціаліст має робочі години (наприклад, понеділок-п'ятниця прийом з 9:00 до 18:00, субота та неділя - вихідні). 
Протягом робочого дня спеціаліст приймає клієнтів (пацієнтів), що записані до нього. Кожен прийом триває годину та починається на початку години (наприклад, з 9:00 до 10:00 Іванов, з 10:00 до 11:00 Сидоренко, з 12:00 до 13:00 Петров). 
Програма має надавти можливість шукати вільні "вікна" у лікаря на тиждень (у попередньому прикладі - з 11:00 до 12:00), створювати запис для пацієнта на обраний час (якщо цей час вільний), переносити запис на інший вільний час або до іншого лікаря, скасовувати запис.
Усі дані (розклад роботи лікарів, заплановані записи тощо) програма має зберігати у JSON файлах, які мають оновлюватися при кожній зміні інформації. На початку роботи програма, за наявності торрібних файлів, має завантажувати усі раніше створені дані.
Після написання програми створіть 10 тестових спеціалістів (лікарів) з їхнім розкладом роботи. Створіть функцію, яка додаватиме певну кількість записів до цих спеціалістів (кількість передається цій функції як аргумент, кожен запис виконується на перше вільне вікно, прізвище пацієнта будь-яке, можна рандомний рядок). Задекоруйте її декоратором, який засікатиме час виконання функції. Створіть 10, 100, 1000 записів. За результатами виводу оцініть час, необхідний для створення одного запису у кожному випадку 
'''

import json, os, os.path



class Doctor:
    doctors = []
    def __init__(self, doctor_name, day_of_week, date, client):
        self.doctor_name = doctor_name
        self.day_of_week = day_of_week
        self.date = date
        self.client = client
        Doctor.doctors.append(self)
        self.dump_json()

    def dump_json(self):
        file = f'{self.doctor_name}_{self.day_of_week}.json'
        path_json = os.path.join(os.getcwd(), 'Doctors', file)
        tmp_list = [t.__dict__ for t in self.doctors if t.doctor_name == self.doctor_name]

        with open(path_json, 'w', encoding='utf-8') as file:
            json.dump(tmp_list, file, indent=4)
            file.close()

t = Doctor('Ivanov', 'Monday', '8', 'Client1')
e = Doctor('Ivanov', 'Monday', '9', 'Client2')
d = Doctor('Petrov', 'Monday', '8', 'Client2')

