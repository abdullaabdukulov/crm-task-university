from django.db import connection
from contextlib import closing


def dict_fetch_all(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]


def dict_fetch_one(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def get_faculty():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from adminapp_faculty;""")
        faculties = dict_fetch_all(cursor)
        return faculties


def get_kafedra():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from adminapp_kafedra;""")
        kafedra = dict_fetch_all(cursor)
        return kafedra


def get_subject():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM adminapp_subject;""")
        subject = dict_fetch_all(cursor)
        return subject


def get_teacher():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT 
                                adminapp_teacher.id as id,
                                first_name,
                                last_name,
                                age,
                                adminapp_kafedra.name as kafedra,
                                adminapp_subject.name as subject,
                                adminapp_teacher.image as image
                          FROM 
                                adminapp_teacher
                          LEFT JOIN 
                                adminapp_kafedra
                          ON adminapp_teacher.kafedra_id=adminapp_kafedra.id
                          LEFT JOIN 
                                adminapp_subject
                          ON adminapp_teacher.subject_id=adminapp_subject.id""")
        teacher = dict_fetch_all(cursor)
        return teacher


def get_group():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM adminapp_group;""")
        group = dict_fetch_all(cursor)
        return group


def get_student():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT
                                adminapp_student.id as id,
                                adminapp_student.first_name as first_name,
                                adminapp_student.last_name as last_name,
                                adminapp_student.age as age,
                                adminapp_group.name as st_group,
                                adminapp_student.image as image 
                          FROM 
                                adminapp_student
                          LEFT JOIN 
                                    adminapp_group 
                          ON adminapp_student.group_id=adminapp_group.id;""")
        student = dict_fetch_all(cursor)
        return student

