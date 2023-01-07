from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_STUDENTS = 40
NUMBER_GROUPS = ["Group A",
                 "Group B",
                 "Group C"
                 ]

NUMBER_LESONS = ["History",
                 "Philosophy",
                 "Foreign language",
                 "Geography",
                 "Economic",
                 ]
NUMBER_PROFESORS = 4



def generate_fake_data(number_students,number_profesors) -> tuple():
    fake_students = []
    fake_professors = []

    fake_data = faker.Faker()

    for _ in range(number_students):
        fake_students.append(fake_data.name())

    for _ in range(number_profesors):
        fake_professors.append(fake_data.name())

    return fake_students, fake_professors

def prepare_group_table(number_group):
    for_groups = []
    for group in number_group:
        for_groups.append((group, ))
    return for_groups

def prepare_students_table(fake_students):
    for_students = []

    for student in fake_students:
        for_students.append((randint(1,len(NUMBER_GROUPS)), student ))

    return for_students

def prepare_lessons_table(number_lessons):
    for_lessons =[]

    for lesson in number_lessons:
        for_lessons.append(( randint(1,NUMBER_PROFESORS), lesson))

    return for_lessons

def prepare_professor_table(fake_professors):
    for_professors = []

    for profesor in fake_professors:
        for_professors.append((profesor, ))

    return for_professors

def prepare_grades_table():
    for_grades = []


    for i in range(1, NUMBER_STUDENTS+1):

        for grades in range(1, randint(18,20)):
            date = datetime(2022, randint(1, 12), randint(1, 28)).date()
            grade = randint(1,5)
            lesons_id = randint(1,len(NUMBER_LESONS))
            for_grades.append((date, grade, lesons_id, i))

    return for_grades






def insert_data_to_db(group, students, lessons, profesors, grades) -> None:

    with sqlite3.connect('study.db') as con:

        cur = con.cursor()

        sql_to_groups = """INSERT INTO groups(group_name)
                               VALUES (?)"""

        cur.executemany(sql_to_groups, group)

        sql_to_students = """INSERT INTO students(group_id, student_name)
                               VALUES (?, ?)"""

        cur.executemany(sql_to_students, students)

        sql_to_lessons = """INSERT INTO lesons(id_profesor, leson_name)
                              VALUES (?, ?)"""

        cur.executemany(sql_to_lessons, lessons)

        sql_to_profesors = """INSERT INTO professors(profesor_name)
                              VALUES (?)"""

        cur.executemany(sql_to_profesors,profesors)

        sql_to_grades = """INSERT INTO graduates(date_of, grade, leson_id, student_id)
                              VALUES (?, ?, ?, ?)"""

        cur.executemany(sql_to_grades, grades)

        con.commit()


if __name__ == "__main__":
    fake_students, fake_profesors = generate_fake_data(NUMBER_STUDENTS,NUMBER_PROFESORS)
    group = prepare_group_table(NUMBER_GROUPS)
    students = prepare_students_table(fake_students)
    lessons = prepare_lessons_table(NUMBER_LESONS)
    profesors = prepare_professor_table(fake_profesors)
    grades = prepare_grades_table()
    insert_data_to_db(group,students,lessons,profesors,grades)