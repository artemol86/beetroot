
# 3. За допомогою фреймворку Flask реалізувати простий сервер, який буде мати два url:
#     - "/" - повертає список повних імен всіх персон (first_name + last_name), у текстовому представленні.
#     - "/person/<int:person_id>" - повертає тектове представлення інформації про одного користувача.


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
    def get_list(cls):
        return cls.list_per

    @classmethod
    def list_to_json(cls):
        person_list = [t.__dict__ for t in cls.list_per]
        return json.dumps(person_list)

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

    def to_json(self):
        return json.dumps(self.__dict__)


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

    print(per.list_to_json())

