# Загальна мета заняття - розробити основні елементи сайта, що надає сервіс конструктора резюме для користувачів.
# Ідея полягає в тому, що користувач може додати свій обліковий запис, додавати/змінювати/видаляти контакти,
# навички та досвід роботи, а система згенерує сторінку з його резюме.
#
# Для реалізації задуму треба:
# 1. Реалізвуати класи, які будуть виконувати роль моделей даних.
#     - class Skill - описує одну за навичок користувача. Навички можуть бути трьох категорій (category): технології (technologies),
#     методолії (methodologies) та мови (languages). Кожна навичка характеризується такими параметрами: назва (name),
#     досвід (experience) - кількість років використання цієї технології/методолгії/мови, рівень володіння навичкою
#     (level) - вибір з п'яти можливих варіантів: beginner, junior, middle, senior, expert.
#     - class Contact - описує контактні дані користувача. Описується полями тип (contact_type) - вибір з варіантів 'phone' та 'email';
#     та значення (value) - конкретна мейл-адреса або номер телефону користувача.
#     - class JobExperience - описує доствід роботи користувача. Харкатеризується атрибутами: дата початку роботи (start_date),
#     дата завершення роботи (end_date), компанія (company), посада (position).
#     - class Person - описує особу самого користувача. Має атрибути  ім'я (first_name), прізвище (last_name), дата народження (birth_date),
#     а також списки контактів (об'єкти класу Contact), навичок (об'єкти класу Skill) та досвіду роботи (об'єкти класу JobExperience).
#     Кожен об'єкт класу має також атрибут id - унікальний ідентифікатор користувача в системі.




# 2. Реалізувати відповідні методи для класу Person:
#     - Для кожного зі списків (контакти, навички, досвід роботи) мають бути реалізовані методи додавання (add),
#     видалення (delete) та оновлення (update) елементів списку. Для реалізації цих методів можливо буде необхідне додавання вспоміжних
#     атрибутів для кожного класу.
#     - Реалізвуати методи збереження інфомації про об'єкт класу Person разом з усіма вкладеними
#     об'єктами у JSON файл та завантаження JSON файлу із створенням всіх вкладених об'єктів.
#     - Реалізувати метод, який представляє список skills персони, розбитий за категоріями. Метод має вовертати словник,
#     де ключами є категорії навичок, а значеннями - списки об'єктів навичок персони,
#     що належать до цієї категорії, відсортовані за зменшенням досвіду (навичка з найбільшим значенням досвіду у цій категорії йде перша).
#     - Реалізувати метод, який сортує досвід роботи персони від найбільш актуального до найбільш давнього
#     (останній досвід роботи йде першим у відсортованому списку, найбільш давній - останнім)

#
# За необхідності можна додавати будь-які службові атрибути та методи для будь-яких класів. Усе рішення має міститися в окремій папці з назвою cv_builder.
# © 2021 GitHub, Inc.
# Terms
# Privacy
# Security
# Status
# Docs
# Contact GitHub
import os
import json
import operator

class Skill:
    list_skill = []
    def __init__(self, category, name, experience, level):
        self.category = category
        self.name = name
        self.experience = experience
        self.level = level
        Skill.list_skill.append(self)
        self.id = len(Skill.list_skill)

    @classmethod
    def add_skills_obj(cls, dict_skills):
        obj = cls(category=None, name=None, experience=None, level=None)
        for skill in dict_skills:
            setattr(obj, skill, dict_skills[skill])
        return obj


    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, skill):
        if skill in ['technologies', 'methodologies', 'languages']:
            self._category = skill
        else:
            # raise ValueError
            self._category = None

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        if level in ['beginner', 'junior', 'middle', 'senior', 'expert']:
            self._level = level
        else:
            self._level = None


class Contact:
    contacts = []

    def __init__(self, contact_type, value):
        self.contact_type = contact_type
        self.value = value
        Contact.contacts.append(self)

    def __str__(self):
        return f'{self.contact_type} {self.value}'

    @property
    def contact_type(self):
        return self._contact_type

    @contact_type.setter
    def contact_type(self, contact_type):
        if contact_type in ['phone', 'email']:
            self._contact_type = contact_type
        else:
            self._contact_type = None

    @classmethod
    def add_contacts_obj(cls, dict_contacts):
        obj = cls(contact_type=None, value=None)
        for contact in dict_contacts:
            setattr(obj, contact, dict_contacts[contact])
        return obj

class JobExperience:

    def __init__(self, start_date, end_date, company, position):
        self.start_data = start_date
        self.end_data = end_date
        self.company = company
        self.position = position

    @classmethod
    def add_experience_obj(cls, dict_experience):
        obj = cls(start_date=None, end_date=None, company=None, position=None)
        for experience in dict_experience:
            setattr(obj, experience, dict_experience[experience])
        return obj

class Person:
    list_per = []
    def __init__(self, last_name, first_name, birth_date):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.contact = []
        self.skills = []
        self.experience = []
        Person.list_per.append(self)
        self.id = len(Person.list_per)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'


    @classmethod
    def add_person_obj(cls, dict_person):

        method_dict = {
            'contact': Contact.add_contacts_obj,
            'skills': Skill.add_skills_obj,
            'experience': JobExperience.add_experience_obj
        }

        obj = cls(last_name=None, first_name=None, birth_date=None)
        for person in dict_person:
            setattr(obj, person, dict_person[person])
            if person in ['contact', 'skills', 'experience']:
                setattr(obj, person, [method_dict[person](i) for i in dict_person[person]])
        return obj


    def add_contact(self, contact_type, value):
        self.contact.append(Contact(contact_type, value))

    def add_skills(self, category, name, experience, level):
        self.skills.append(Skill(category, name, experience, level))

    def add_experience(self, start_date, end_date, company, position):
        self.experience.append(JobExperience(start_date, end_date, company, position))

    def del_contact(self, val):
        for contact in self.contact:
            if contact.value == val:
                del self.contact[self.contact.index(contact)]

    def del_skills(self, id):
        for skill in self.skills:
            if id == skill.id:
                del self.skills[self.skills.index(skill)]

    def del_experience(self, company):
        for exp in self.experience:
            if company == exp.company:
                del self.experience[self.experience.index(exp)]

    def update_contact(self, contact_type, value, val):
        for cont in self.contact:
            if cont.value == val:
                cont.contact_type = contact_type
                cont.value = value

    def update_skills(self, category, name, experience, level, id):
        for skill in self.skills:
            if skill.id == id:
                skill.category = category
                skill.name = name
                skill.experience = experience
                skill.level = level

    def update_experience(self, start_date, end_date, company, position, val):
        for item in self.experience:
            if item.company == val:
                item.start_date = start_date
                item.end_date = end_date
                item.company = company
                item.position = position

    def dump_json(self):
        file_name = 'person.json'
        path_json = os.path.join(os.getcwd(), 'data', file_name)
        item = {}
        for key, val in self.__dict__.items():
            item[key] = val
            if key in ['contact', 'skills', 'experience']:
                item[key] = [i.__dict__ for i in val]
        with open(path_json, 'w') as file:
            json.dump(item, file)

    @classmethod
    def load_json(cls):
        file_name = 'person.json'
        path_json = os.path.join(os.getcwd(), 'data', file_name)
        with open(path_json, 'r') as file:
            dict_person = json.load(file)

        obj_person = Person.add_person_obj(dict_person)
        return obj_person

    def skills_category(self):
        list_skills = []
        list_key = []
        for skill in self.skills:
            if skill.category in list_key:
                continue
            list_key.append(skill.category)
            skill_category = []
            for item in self.skills:
                if skill.category == item.category:
                    skill_category.append(item)
                    skill_category.sort(key=lambda k: skill.experience)
            list_skills.append({skill.category: skill_category})
        return list_skills

#     - Реалізувати метод, який сортує досвід роботи персони від найбільш актуального до найбільш давнього
#     (останній досвід роботи йде першим у відсортованому списку, найбільш давній - останнім)

    def sort_experience(self):
        return sorted(self.experience, key=operator.attrgetter('end_data'), reverse=True)


per = Person('Petrov', 'Petr', 23)
per1 = Person('as', 'as', 23)
per2 = Person('asdf', 'asdf', 23)
if __name__ == '__main__':

    per = Person('asdf', 'asdf', 23)
    per1 = Person('asdf', 'asdf', 23)
    per2 = Person('asdf', 'asdf', 23)

    per.add_contact('phone', 4567)
    per.add_contact('phone', 78900987)

    per.add_skills('technologies', 'asdfg', 1, 'junior')
    per.add_skills('technologies', 'vbnm', 2, 'junior')
    per.add_skills('methodologies', 'fd', 3, 'junior')
    per.add_skills('languages', 'vb', 4, 'junior')

    per.add_experience(23, 34, 'asd', 'jun')
    per.add_experience(24, 39, 'fgh', 'jun')
    per.add_experience(25, 37, 'jhk', 'jun')
    per.add_experience(26, 38, 'cvb', 'jun')

    # print(per.sort_experience())
    # exp = per.sort_experience()
    # for e in exp:
    #     print(e.end_data)

    # print(per.skills_category())
    # print(per.skills_category()[0]['technologies'][0].experience)
    # print(per.skills_category()[0]['technologies'][1].experience)

    # per.dump_json()
    # print(per.load_json())
    # per4 = Person.load_json()
    # print(per4.skills[0].name)
    # print(per.__dict__)

    # for i in per.contact:
    #     print(i)
    # # per.del_contact(4567)
    # print('----------------------------------------------------------------')
    # # per.del_skills(2)
    # per.update_contact('email', 444444444444444, 4567)
    # per.del_experience('fgh')
    # for m in per.contact:
    #     print(m)
    # for item in per.contact:
    #     print(item)