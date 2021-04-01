def customer_login_check(cursor,email):
    passwd_hash=cursor.execute("SELECT PASSWD FROM CUSTOMER WHERE EMAIL=(?)", email)
    try:
        fetched_hash = passwd_hash.fetchall()[0][0].strip()
        return fetched_hash
    except:
        return 0

def employee_login_check(cursor,email):
    passwd_hash=cursor.execute("SELECT PASSWD FROM EMPLOYEE WHERE EMAIL=(?)", email)
    try:
        fetched_hash = passwd_hash.fetchall()[0][0].strip()
        return fetched_hash
    except:
        return 0