def is_leaf_department(cursor, department_number):
    department_numbers = cursor.fetchall(f"SELECT department_number FROM DEPARTMENT WHERE root_department_number={department_number}" )
    if len(department_numbers) == 0:
