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

def load_students():
	for test_student in TEST_STUDENTS:
		student = STUDENTS.append(dict(zip(student_fields,test_student)))

while True:
	action = input('Desired action:\t')
	if action == 'add':
		add_student()
	elif action == 'avg_age':
		calculate_avg_age()
	elif action == 'load':
		load_students()
	elif action == 'print':
		for student in STUDENTS:
			print_student(student)
	else:
		break
