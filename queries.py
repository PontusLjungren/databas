def is_leaf_department(cursor, department_number):
    cursor.execute(f"SELECT Department_number, title FROM DEPARTMENT WHERE Root_department_number={department_number}")
    child_departments = cursor.fetchall( )
    if len(child_departments) == 0:
        cursor.execute(f"SELECT Title, Product_number, Base_price, Discount_percentage FROM PRODUCT WHERE Department_number={department_number}")
        products = cursor.fetchall()
        applied_discounts = []
        for product in products:
            applied_discounts.append([product[0], product[1], product[2] * (1 - product[3] / 100)])
        return applied_discounts
    return child_departments

def get_discount(cursor, product_number):
    cursor.execute(f"Select Discount_percentage FROM PRODUCT WHERE Product_number={product_number}")
    return cursor.fetchone()

def set_discount(cursor, product_number, new_discount):
    cursor.execute(f"UPDATE PRODUCT SET Discount_percentage={new_discount} WHERE Product_number={product_number}")