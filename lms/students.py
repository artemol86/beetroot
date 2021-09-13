import json
import csv

student_fields = ['first_name', 'last_name', 'email', 'age', 'address', 'gender']
STUDENTS = []

TEST_STUDENTS = [
	['Mary', 'D', 'mail@mail.com', '19', 'Huston', 'F'],
	['John', 'S', 'new_mail@mail.com', '19', 'Huston', 'F'],
	['Andy', 'H', 'more_email@email.com', 'sexteen', 'Brighton', 'M']
]

def add_student():
	student = {}
	for field in student_fields:
		student[field] = input('Enter {}\t'.format(field))
		if field == 'age':
			try:
				int(student['age'])
			except:
				students['age'] = input('Enter age as number\t')
	STUDENTS.append(student)

def calculate_avg_age():
	try:
		total_age = 0
		for student in STUDENTS:
			total_age += int(student['age'])
		average_age = total_age / len(STUDENTS)
		print('Average age is {}'.format(average_age))
	except ValueError:
		print('Can not calculate average age')
	except Exception as e:
		print(e)

def print_student(student):
	for field in student:
		print(field, '\t', student[field])

def print_strudents_list():
    '''Call print_student() for every student in STUDENTS''' 
    pass

def load_students():
	for test_student in TEST_STUDENTS:
		student = STUDENTS.append(dict(zip(student_fields,test_student)))

def dump_students():
	with open('student_data.json', 'w') as file:
		json.dump(STUDENTS,file)

def load_from_json(file_path='student_data.json'):
	with open(file_path, 'r') as readfile:
		STUDENTS = json.load(read_file)

def dump_csv():
	with open('student_data.csv', 'w') as file:
		writer = csv.DictWriter(file, fieldnames=student_fields)
		writer.writeheader()
		for student in STUDENTS:
			writer.writerow(student)

ACTIONS = {
	'add' : add_student,
	'avg_age' : calculate_avg_age,
	'load' : load_students,
	'print' : print_students_list,
	'dump' : dump_students,
	'dump_csv' : dump_csv, 
	'load_json' : load_from_json,
}

while True:
	action = input('Desired action:\t')
	if action in ACTIONS:
		ACTIONS.get(actions)()
	else:
		break
