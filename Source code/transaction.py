from datetime import datetime
from time import sleep
def transact(cursor, from_acc_no, to_acc_no, tot, trans_amt, trans_msg):
    trans_amt=float(trans_amt)
    from_acc_no=int(from_acc_no)
    to_acc_no=int(to_acc_no)
    temp=-1
    try:
        cursor.execute('LOCK TABLES ACCOUNT WRITE, TRANSACTIONS WRITE')

        to_amt = float(cursor.execute('SELECT BALANCE FROM ACCOUNT WHERE ACC_NO = (?)',to_acc_no).fetchall()[0][0])
        from_amt = float(cursor.execute('SELECT BALANCE FROM ACCOUNT WHERE ACC_NO = (?)',from_acc_no).fetchall()[0][0])

        final_to_amt = to_amt + trans_amt
        final_from_amt = from_amt - trans_amt

        cursor.execute('UPDATE ACCOUNT SET BALANCE = (?) WHERE ACC_NO = (?);',final_to_amt,to_acc_no)
        sleep(5)
        cursor.execute('UPDATE ACCOUNT SET BALANCE = (?) WHERE ACC_NO = (?);',final_from_amt,from_acc_no)
        temp=1


    except Exception as e:
        print("EXception---->")
        print(e)
        cursor.execute('ROLLBACK')
        temp= -1


    finally:
        tid = (cursor.execute('select count(*) from transactions for update').fetchall()[0][0]) + 1
        tid = str(tid)
        tid = tid.zfill(6)
        tid = 'TR' + tid
        if temp == 1:
            cursor.execute("INSERT INTO TRANSACTIONs VALUES((?),(?),(?),(?),(?),(?),(?),(?))", tid, from_acc_no, to_acc_no,datetime.now(), tot, trans_amt, trans_msg, 'SUCCESS')
            cursor.execute("COMMIT")
            cursor.execute('UNLOCK TABLES')
            return 1
        else:
            cursor.execute("INSERT INTO TRANSACTIONs VALUES((?),(?),(?),(?),(?),(?),(?),(?))", tid, from_acc_no,to_acc_no, datetime.now(), tot, trans_amt, trans_msg, 'FAILED')
            cursor.execute("COMMIT")
            cursor.execute('UNLOCK TABLES')
            return -1
