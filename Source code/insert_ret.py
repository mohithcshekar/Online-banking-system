def insert_emp(cursor, emp_id,name,email,passwd, br_code):
    try:
        cursor.execute('INSERT INTO EMPLOYEE VALUES (?,?,?,?,?,?)',emp_id,name,email,passwd, br_code,"TELLER")
        cursor.commit() #EMP_ID, NAME, EMAIL, PASSWD, BRANCH_CODE, DESIGNATION
        return 1
    except:
        return -1


def cus_update(cursor, cust_id,passwd):
    passwd = '"%s"' % passwd
    cust_id = '"%s"' % cust_id
    state='UPDATE CUSTOMER set passwd = ' + passwd +'WHERE CUST_ID = '+cust_id
    cursor.execute(state)
    cursor.commit()


def insert_customer(cursor, cust_id,f_name,l_name,palace,uid,mob_no,email,passwd,acc_no, balance, branch_code):
    try:
        cursor.execute('INSERT INTO CUSTOMER VALUES (?,?,?,?,?,?,?,?)', cust_id, f_name, l_name, palace, uid, mob_no, email, passwd)
        cursor.execute('INSERT INTO ACCOUNT VALUES (?,?,?,?)', cust_id, acc_no, balance, branch_code)
        cursor.commit()
        return 1
    except:
        cursor.rollback()
        return -1


def insert_account(cursor, cust_id,acc_no,balance,branch_code):
    cursor.execute('INSERT INTO ACCOUNT VALUES (?,?,?,?)',cust_id,acc_no,balance,branch_code)
    cursor.commit()


def insert_debit_card(cursor, acc_no,card_no,expire_date,cvv,pincode):
    cursor.execute('INSERT INTO DEBIT_CARD VALUES (?,?,?,?,?)', acc_no, card_no, expire_date, cvv, pincode)
    cursor.commit()


def ret_table_vals(cursor,table_name,where,cond):
    cond='"%s"' %cond
    statement="SELECT * FROM "+table_name+" WHERE "+where+" = "+cond
    obtained_vals=cursor.execute(statement).fetchall()
    try:
        return obtained_vals[0]
    except :
        return -1


def delete_card(cursor, table,where,card_no):
    card_no = str(card_no)
    card_no = '"%s"' % card_no
    state = "DELETE FROM " + table+"  WHERE " + where + " = " + card_no
    cursor.execute(state)
    cursor.commit()
    if cursor.rowcount == 0:
        return -1
    else:
        return 0


def cus_join_acc(cursor, trans_to_acc):
    statement="SELECT * FROM(CUSTOMER  NATURAL JOIN ACCOUNT A where A.ACC_NO = "+trans_to_acc
    obtained_vals = cursor.execute(statement)
    return obtained_vals[0]
