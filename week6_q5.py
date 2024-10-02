def get_student_data():
    with open('Marks.data','w') as file:
        num_students = int(input('How many students to enter: '))
        for i in range(num_students):
            print(f'\nEnter student details, student{i+1}:')
            name = input('Name: ')
            roll_no = int(input('Roll No.: '))
            cgpa = float(input('CGPA: '))
            file.write(f'Name: {name}, Roll No.: {roll_no}, CGPA: {cgpa}\n')

        print('\nMarks.data file successfully updated.')

get_student_data()