import pyodbc
import login_check, insert_ret,transaction, analysis, chart
from sys import exit
from flask import Flask, request, render_template,redirect
from hashlib import md5
from datetime import datetime
import atexit
import time
#from waitress import serve

cust_id=f_name=l_name=place=uid=mob_no=acc_no=balance=br_code=email=password=tot=''
trans_to_name=trans_to_acc=trans_ifsc=trans_mob_no=trans_remarks=error_msg=''

app = Flask(__name__)

try:
    cnxn = pyodbc.connect('DRIVER={MySQL ODBC 8.0 Unicode Driver};SERVER=localhost:3306;DATABASE=BANK;UID=root;PWD=GROWmore11')
    cursor = cnxn.cursor()
    print("DBMS server connection successful")
except :
    print("DBMS server connection unsuccessfull")
    exit(1)

def login_flush():
    global cust_id, f_name, l_name, place, uid, mob_no, acc_no, balance, br_code, email, password,tot,\
        trans_to_name, trans_to_acc, trans_ifsc, trans_mob_no, trans_remarks,error_msg,desig
    cust_id = f_name = l_name = place = uid = mob_no = acc_no = balance = br_code = email = password = tot = ''
    trans_to_name = trans_to_acc = trans_ifsc = trans_mob_no = trans_remarks = error_msg = desig = ''


@app.route('/')
@app.route('/index.html')
def index():
    login_flush()
    return render_template('index.html')



@app.route('/customer-login.html')
def customer_login():
    login_flush()
    return render_template('customer-login.html')
@app.route('/customer-login.html', methods=['GET','POST'])
def customer_login_post():
    global cust_id,f_name,l_name,place,uid,mob_no,acc_no,balance,br_code,email,password
    email=request.form["email"]
    password=request.form["passwd"]
    crct_hash=login_check.customer_login_check(cursor,email)
    if crct_hash == md5(password.encode()).hexdigest() :
        cust_table=insert_ret.ret_table_vals(cursor, "CUSTOMER","EMAIL",email) #cursor,table_name,where,cond
        cust_id=str(cust_table[0])
        f_name=str(cust_table[1])
        l_name=str(cust_table[2])
        place=str(cust_table[3])
        uid=str(cust_table[4])
        mob_no=str(cust_table[5])
        acc_table = insert_ret.ret_table_vals(cursor, "ACCOUNT","CUST_ID",cust_id)
        acc_no=str(acc_table[1].to_eng_string())
        balance=str(acc_table[2].to_eng_string())
        br_code=str(acc_table[3])
        return redirect ("/customer-dashboard.html")
    else:
        return redirect("error.html")




@app.route('/customer-register-before.html')
def customer_register_before():
    return render_template('customer-register-before.html')
@app.route('/customer-register-before.html', methods=['POST'])
def customer_register_before_post():
    global cust_id, f_name, l_name, place, uid, mob_no, acc_no, email, password
    login_flush()
    cust_id = request.form['cust_id']
    acc_no = request.form['acc_no']
    ch1=insert_ret.ret_table_vals(cursor, "CUSTOMER", "CUST_ID", cust_id)
    ch2=insert_ret.ret_table_vals(cursor, "ACCOUNT", "ACC_NO", acc_no)
    if ch1==-1 and ch2==-1:
        return redirect("error.html")
    else:
        return redirect('customer-register.html')



@app.route('/customer-register.html')
def customer_register():
    global cust_id, f_name, l_name, place, uid, mob_no, acc_no, email, password
    cust_table = insert_ret.ret_table_vals(cursor, "CUSTOMER", "CUST_ID", cust_id)  # cursor,table_name,where,cond
    f_name = str(cust_table[1])
    l_name = str(cust_table[2])
    place = str(cust_table[3])
    mob_no = str(cust_table[5])
    email = str(cust_table[6])
    return render_template('customer-register.html',f_name=f_name,l_name=l_name,place=place,mob_no=mob_no,cust_id=cust_id,email=email)
@app.route('/customer-register.html', methods=['POST'])
def customer_register_post():
    global cust_id, f_name, l_name, place, uid, mob_no, acc_no, email, password
    password= request.form['passwd']
    passwd=md5(password.encode()).hexdigest()   #Hashing the password
    card_no=request.form['card_no']
    expire_date= request.form['expire_date']
    cvv= request.form['cvv']
    pin= request.form['pin']
    #print("_____> here"+passwd+card_no+expire_date+cvv+pin)
    insert_ret.cus_update(cursor, cust_id,passwd)
    insert_ret.insert_debit_card(cursor, acc_no, card_no, expire_date, cvv, pin)
    return render_template('index.html')


@app.route('/customer-dashboard.html')
def customer_dashboard():
    global email
    if len(email)==0:
        return redirect("error.html")
    acc_table = insert_ret.ret_table_vals(cursor, "ACCOUNT", "CUST_ID", cust_id)
    balance = str(acc_table[2].to_eng_string())
    return render_template("customer-dashboard.html",f_name=f_name,l_name=l_name,place=place,uid=uid,mob_no=mob_no,balance=balance,br_code=br_code,acc_no=acc_no, cust_id=cust_id, email=email )

def statements_page():
    global acc_no
    itr = cursor.execute('SELECT TRANS_ID, FROM_ACC , TO_ACC, TIME_DATE, TYPE_OF_TRANS, AMOUNT, STATUS FROM TRANSACTIONS WHERE FROM_ACC = (?) OR TO_ACC=(?)',acc_no, acc_no).fetchall()
    stats = []
    for row in itr:
        stats.append(list(map(str, list(row))))
    return stats
@app.route("/statements.html")
def statements():
    global acc_no
    if len(email)==0:
        return redirect("error.html")
    return render_template("statements.html",stats=statements_page())


@app.route('/tot.html')
def type_of_transact():
    global email
    if len(email)==0:
        return redirect("error.html")
    return render_template("tot.html")
@app.route('/tot.html',methods=["GET",'POST'])
def type_of_transact_post():
    global email,tot
    if len(email)==0:
        return redirect("error.html")
    global tot
    tot= request.form["tot"]
    if tot=="card":
        return redirect("debit-trans.html")
    else:
        return redirect("normal-trans.html")


@app.route('/normal-trans.html')
def normal_transaction():
    global email
    if len(email) == 0:
        return redirect("error.html")
    return render_template("normal-trans.html",tot=tot.upper())
@app.route('/normal-trans.html', methods=['POST'])
def normal_transaction_post():
    global email, acc_no,tot, error_msg
    if len(email) == 0:
        return redirect("/error.html")
    trans_to_name=str(request.form['trans_to_name'])
    trans_to_acc=str(request.form['trans_to_acc'])
    trans_ifsc=str(request.form['trans_ifsc'])
    trans_amt = str(request.form['trans_amt'])
    trans_mob_no=str(request.form['trans_mob_no'])
    trans_remarks=str(request.form['trans_remarks'])
    check_acc = insert_ret.ret_table_vals(cursor, "ACCOUNT", "ACC_NO", trans_to_acc)
    check_ifsc = insert_ret.ret_table_vals(cursor, "BRANCH", "IFSC_CODE",trans_ifsc)
    #print(" current thread id: " + str(thread.get_ident()))
    if check_acc == -1 or check_ifsc==-1:
        return redirect("error.html")
    #print('obtained normal: ' + trans_to_name + trans_to_acc + trans_ifsc +trans_mob_no + trans_remarks)
    else:
        trans_msg="To : "+trans_to_name+",Transaction remarks "+trans_remarks+", Mob No: "+trans_mob_no
        #cursor.execute("LOCK TABLES ACCOUNT WRITE, DEBIT_CARD WRITE, TRANSACTIONS WRITE")
        trans_flag=transaction.transact(cursor,acc_no, trans_to_acc,tot.upper(),trans_amt,trans_msg)
        #cursor.execute("UNLOCK TABLES")
        #(cursor, from_acc_no, to_acc_no, tot, trans_amt, trans_msg)
        #print("return ---"+trans_flag)
        if trans_flag == 1:
            #print(" current thread id: " + str(thread.get_ident()))
            return render_template("success-trans.html",dash_url="customer-dashboard.html")
        elif trans_flag ==-2:
            error_msg="You don't have sufficient balance."
            return redirect("error-trans.html")
        elif trans_flag == -1:
            error_msg="Transaction failed. Because provided information is wrong."
            return redirect("error-trans.html")


@app.route('/debit-trans.html')
def debit_transaction_():
    global email,acc_no
    if len(email) == 0:
        return redirect("error.html")
    return render_template("debit-trans.html")
@app.route('/debit-trans.html', methods=['GET','POST'])
def debit_transaction_post():
    global email,tot,error_msg
    if len(email) == 0:
        return redirect("error.html")
    trans_card=str(request.form['trans_card'])
    trans_expiry=str(request.form['trans_expiry'])
    trans_cvv = str(request.form['trans_cvv'])
    trans_pin = str(request.form['trans_pin'])
    trans_to_name=str(request.form['trans_to_name'])
    trans_to_acc=str(request.form['trans_to_acc'])
    trans_amt = str(request.form['trans_amt'])
    trans_mob_no=str(request.form['trans_mob_no'])
    trans_remarks=str(request.form['trans_remarks'])
    check_acc=insert_ret.ret_table_vals(cursor,"ACCOUNT","ACC_NO",trans_to_acc)
    if check_acc==-1:
        error_msg = " Wrong account information."
        return redirect("/error-trans.html")

    else:
        trans_msg = "To : " + trans_to_name + ",Transaction remarks " + trans_remarks + ", Mob No: " + trans_mob_no
        #cursor.execute("LOCK TABLES ACCOUNT WRITE, DEBIT_CARD WRITE, TRANSACTIONS WRITE")
        trans_flag = transaction.transact(cursor, acc_no, trans_to_acc, tot.upper(), trans_amt, trans_msg)
        #cursor.execute("UNLOCK TABLES;")
        check_card = insert_ret.ret_table_vals(cursor, "debit_card", "CARD_NO", trans_card)
        if check_card != -1:
            if trans_flag == 1:
                return render_template("success-trans.html", dash_url="customer-dashboard.html")
            elif trans_flag == -1:
                error_msg = "You don't have sufficient balance."
                return redirect("error-trans.html")
            elif trans_flag == -2:
                error_msg = "Transaction failed. Because provided information is wrong."
                return redirect("error-trans.html")
        else:
            error_msg = " Incorrect debit card information."
            return redirect("/error-trans.html")


@app.route('/employee-login.html')
def employee_login():
    login_flush()
    return render_template('employee-login.html')
@app.route('/employee-login.html', methods=['GET','POST'])
def employee_login_post():
    global cust_id,f_name,l_name,place,uid,mob_no,acc_no,balance,email,password,desig,identity
    email=request.form["email"]
    password=request.form["passwd"]
    crct_hash=login_check.employee_login_check(cursor,email)
    if crct_hash == md5(password.encode()).hexdigest() :
        emp_table=insert_ret.ret_table_vals(cursor, "EMPLOYEE","EMAIL",email) #cursor,table_name,where,cond
        emp_id=str(emp_table[0])
        f_name=str(emp_table[1])
        #br_code=str(emp_table[4])
        desig = str(emp_table[5])
        desg=cursor.execute("SELECT DESIGNATION FROM EMPLOYEE WHERE EMAIL = (?)", email)
        itr = cursor.fetchall()
        itr=itr[0][0]
        if itr == "Manager":
            identity=1
            return redirect("/manager-dashboard.html")
        else:
            identity=0
            return redirect ("/employee-dashboard.html")
    else:
        return redirect("error.html")

@app.route("/employee-dashboard.html")
def employee_dashboard():
    if len(email)==0:
        return redirect("error.html")
    return render_template("employee-dashboard.html")

@app.route("/manager-dashboard.html")
def manager_dashboard():
    if len(email)==0:
        return redirect("error.html")
    return render_template("manager-dashboard.html")

@app.route("/notifications.html")
def notifications():
    closed_accs=[]
    itr=cursor.execute("SELECT * FROM CLOSED_ACC").fetchall()
    for row in itr:
        closed_accs.append(list(map(str, list(row))))
    return render_template("notifications.html",stats=closed_accs)

@app.route("/emp-statements.html")
def employee_statements():
    if len(email)==0:
        return redirect("error.html")
    return render_template("emp-statements.html")
@app.route('/emp-statements.html', methods=['GET','POST'])
def employee_statements_post():
    global acc_no
    acc_no=request.form["acc_no"]
    return render_template("statements.html",stats=statements_page())


@app.route("/emp-trans.html")
def employee_trans():
    if len(email)==0:
        return redirect("error.html")
    return render_template("emp-trans.html")
@app.route('/emp-trans.html', methods=['GET','POST'])
def employee_trans_post():
    global acc_no,trans_to_name,trans_to_acc,tot,amt,trans_remarks,identity,dash_url
    trans_to_name = str(request.form["trans_to_name"])
    acc_no = str(request.form["acc_no"])
    trans_to_acc =str(request.form["trans_to_acc"])
    tot = str(request.form["tot"])
    trans_amt = str(request.form["amt"])
    trans_remarks = str(request.form["trans_remarks"])
    trans_msg = "To : " + trans_to_name + ",Transaction remarks " + trans_remarks
    #cursor.execute("LOCK TABLES ACCOUNT WRITE, DEBIT_CARD WRITE, TRANSACTIONS WRITE")
    trans_flag = transaction.transact(cursor, acc_no, trans_to_acc, tot.upper(), trans_amt, trans_msg)
    #cursor.execute("UNLOCK TABLES")
    if trans_flag == -1:
        return redirect("/error-trans.html")
    else:
        if identity==1:
            dash_url="manager-dashboard.html"
        else:
            dash_url = "employee-dashboard.html"
        return render_template("/success-trans.html",dash_url=dash_url)


@app.route("/card-block.html")
def card_block():
    if len(email)==0:
        return redirect("card-block.html")
    return render_template("card-block.html")
@app.route('/card-block.html', methods=['GET','POST'])
def card_block_post():
    global card_no,identity
    card_no = request.form["card_no"]
    resp=insert_ret.delete_card(cursor, "DEBIT_CARD","CARD_NO",card_no)
    if resp == -1:
        global error_msg
        error_msg = "Invalid Debit card number."
        #print("in function : "+error_msg)
        return redirect("/error-trans.html")
    else:
        msg1 = "DEBIT CARD BLOCKED SUCCESSFULLY"
        msg2="Debit card blocked successfully. User can register once again to continue to use debit card once again"
        if identity==1:
            dash_url="manager-dashboard.html"
        else:
            dash_url="employee-dashboard.html"
        return render_template("block-success.html",msg1=msg1,msg2=msg2,dash_url=dash_url)

@app.route("/close-acc.html")
def close_acc():
    if len(email)==0:
        return redirect("error.html")
    return render_template("close-acc.html")
@app.route('/close-acc.html', methods=['GET','POST'])
def close_acc_post():
    global acc_no,identity
    cus_no = request.form["cus_no"]
    reason = request.form["reason"]
    resp=insert_ret.delete_card(cursor, "CUSTOMER","CUST_ID",cus_no)
    if resp == -1:
        global error_msg
        error_msg = "Invalid Account number."
        return redirect("/error-trans.html")
    else:
        reason = '"%s"' % reason
        cursor.execute("UPDATE CLOSED_ACC SET REASON= (?) WHERE CUST_ID = (?)",reason,cus_no)
        cursor.execute("UPDATE CLOSED_ACC SET TIME_DATE= (?) WHERE CUST_ID = (?)", datetime.now(), cus_no)
        cursor.commit()
        msg1 = "ACCOUNT CLOSED SUCCEFULLY"
        msg2="User account closed successfully"
        if identity==1:
            dash_url="manager-dashboard.html"
        else:
            dash_url="employee-dashboard.html"
        return render_template("block-success.html",msg1=msg1,msg2=msg2,dash_url=dash_url)

@app.route("/open-acc.html")
def open_acc():
    if len(email)==0:
        return redirect("error.html")
    return render_template("open-acc.html")
@app.route('/open-acc.html', methods=['GET','POST'])
def open_acc_post():
    c_fname = str(request.form["c_fname"])
    c_lname = str(request.form["c_lname"])
    c_place = str(request.form["c_place"])
    c_uid = str(request.form["c_uid"])
    c_mob = str(request.form["c_mob"])
    c_email = str(request.form["c_email"])
    c_passwd=str(request.form["c_passwd"])
    c_passwd=md5(c_passwd.encode()).hexdigest()
    c_cuid = str(request.form["c_cuid"])
    c_accno = int(request.form["c_accno"])
    c_amt = int(request.form["c_amt"])
    c_brcode = str(request.form["c_brcode"])
    return

@app.route("/e-signup.html")
def e_signup():
    if len(email)==0:
        return redirect("error.html")
    return render_template("e-signup.html")
@app.route('/e-signup.html', methods=['GET','POST'])
def e_signup_post():
    global emp_name,emp_id,email, passwd, br_code,error_msg,dash_url
    emp_name = str(request.form["emp_name"])
    emp_id1 = str(request.form["emp_id"])
    email1 = str(request.form["email"])
    passwd1 = str(request.form["passwd"])
    passwd1=md5(passwd1.encode()).hexdigest()
    br_code = str(request.form["br_code"])
    #print("here-------",emp_id1, emp_name,email1, passwd1, br_code)
    emp_res=insert_ret.insert_emp(cursor,emp_id1, emp_name,email1, passwd1, br_code) #EMP_ID, NAME, EMAIL, PASSWD, BRANCH_CODE, DESIGNATION
    if emp_res==-1:
        error_msg="Addition of employee failed. Please recheck the form"
        return redirect("/error-trans.html")
    else:
        msg1 = "ACCOUNT CREATED SUCCEFULLY"
        msg2 = "Employee added successfully"
        dash_url="manager-dashboard.html"
        return render_template("block-success.html", msg1=msg1, msg2=msg2,dash_url=dash_url)


@app.route("/analyze.html")
def analyze():
    x1,y1=chart.chart_trans(cursor)
    p1,p2,p3,p4,p5=chart.chart_range(cursor)
    return render_template("analyze.html",x1=x1,y1=y1,p1=p1,p2=p2,p3=p3,p4=p4,p5=p5)
@app.route('/analyze.html', methods=['GET','POST'])
def analyze_post():
    f_amt=str(request.form["f_amt"])
    f_acc=str(request.form["f_acc"])
    f_trans=str(request.form["f_trans"])
    f_fdate=str(request.form["f_fdate"])
    f_tdate = str(request.form["f_tdate"])
    if request.form.get('b1') == "All accounts":
        cus=analysis.all_accounts(cursor)
        return render_template("analyze_customers.html",cus=cus)

    elif request.form.get('b2') == "Filter list":
        cus=analysis.filter_balance(cursor,f_amt )
        return render_template("analyze_customers.html", cus=cus)

    elif request.form.get('b3') == "Filter account":
        cus=analysis.filter_account(cursor,f_acc )
        return render_template("analyze_customers.html", cus=cus)

    elif request.form.get('b4') == "Specific transaction":
        stats=analysis.filter_transaction(cursor,f_trans )
        return render_template("analyze_trans.html", stats=stats)

    elif request.form.get('b5') == "Filter transactions":
        stats=analysis.filter_trans_date(cursor,f_fdate,f_tdate)
        return render_template("analyze_trans.html", stats=stats)


'''@app.route('/success-trans.html')
def trans_success_page():
    login_flush()
    if len(email)==0:
        return redirect("error.html")
    return render_template("success-trans.html")'''

@app.route('/error.html')
def error_page():
    return render_template("error.html")


@app.route('/error-trans.html')
def error_trans_page():
    global error_msg
    #print("outside function : " + error_msg)
    return render_template("error-trans.html",error_msg=error_msg)





@app.route("/logout")
def logout():
    login_flush()
    return redirect("index.html")

try:
    cursor.execute("CREATE temporary TABLE CLOSED_ACC (CUST_ID CHAR(20) , ACC_NO NUMERIC(11),FIRST_NAME VARCHAR(15),BALANCE NUMERIC(14,4), REASON VARCHAR(50) ,TIME_DATE TIMESTAMP)")
    cursor.commit()
except:
    pass


app.run(debug=True)
#serve(app, host='0.0.0.0', listen="*:8080 *:6543", threads=5)
@atexit.register
def at_last():
    cursor.close()
    cnxn.close()
    print("DBMS server termination successfull ")
