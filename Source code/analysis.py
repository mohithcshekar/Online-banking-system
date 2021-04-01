def all_accounts(cursor):
    cursor.execute("SELECT CUST_ID, FIRST_NAME, LAST_NAME, MOB_NO, ACC_NO, BALANCE FROM CUSTOMER_DETAILS")
    itr = cursor.fetchall()
    cus=[]
    for row in itr:
        cus.append(list(map(str, list(row))))
    return cus


def filter_balance(cursor,amt):
    amt=float(amt)
    cursor.execute("SELECT CUST_ID, FIRST_NAME, LAST_NAME, MOB_NO, ACC_NO, BALANCE FROM CUSTOMER_DETAILS WHERE BALANCE >= (?) ",amt)
    itr = cursor.fetchall()
    cus=[]
    for row in itr:
        cus.append(list(map(str, list(row))))
    return cus


def filter_account(cursor,f_acc):
    f_acc = float(f_acc)
    cursor.execute(
        "SELECT CUST_ID, FIRST_NAME, LAST_NAME, MOB_NO, ACC_NO, BALANCE FROM CUSTOMER_DETAILS WHERE ACC_NO = (?) ",f_acc)
    itr = cursor.fetchall()
    cus = []
    for row in itr:
        cus.append(list(map(str, list(row))))
    return cus


def filter_transaction(cursor, trans_id):
    trans_id = "%s" % trans_id
    cursor.execute("SELECT * FROM TRANSACTION_DETAILS WHERE TRANS_ID = (?) ",trans_id)
    itr = cursor.fetchall()
    stats = []
    for row in itr:
        stats.append(list(map(str, list(row))))
    return stats

def filter_trans_date(cursor,f_fdate,f_tdate):
    f_fdate = "%s" % f_fdate
    f_tdate = "%s" % f_tdate
    cursor.execute("SELECT * FROM TRANSACTION_DETAILS WHERE TIME_DATE BETWEEN (?) AND (?) ", f_fdate,f_tdate)
    itr = cursor.fetchall()
    stats = []
    for row in itr:
        stats.append(list(map(str, list(row))))
    return stats
