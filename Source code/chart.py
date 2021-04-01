import datetime

def chart_trans(cursor):
    x1 = []
    total = 0
    y1 = []
    '''for z in range(0, 5):
        x1.append(str((datetime.datetime.today() - datetime.timedelta(days=z)).date()))'''
    cursor.execute("SELECT DISTINCT DATE(TIME_DATE) FROM TRANSACTION_DETAILS order by TIME_DATE desc LIMIT 5")
    itr = cursor.fetchall()
    stats = []
    for row in itr:
        stats.append(list(map(str, list(row))))
    x1 = stats
    for date in stats:
        date = "%s" % date[0]
        cursor.execute("SELECT AMOUNT FROM TRANSACTION_DETAILS WHERE DATE(TIME_DATE) = (?)", date)
        itr1 = cursor.fetchall()
        stats1 = []
        for row in itr1:
            stats1.append(list(map(str, list(row))))
        for stat in stats1:
            total += float(stat[0])
        y1.append(total)
    return x1, y1

def chart_range(cursor):
    cursor.execute("SELECT AMOUNT FROM TRANSACTION_DETAILS")
    itr=cursor.fetchall()
    stats=[]
    for row in itr:
        stats.append((list(map(str, list(row)))))
    p1=p2=p3=p4=p5=0
    for stat in stats:
        temp=float(stat[0])
        if temp in range(1,500):#1-499, 500-1000, 1000-2000, >20000
            p1+=1
        elif temp in range(500,1000):#1-499, 500-1000, 1000-2000, >20000
            p2+=1
        elif temp in range(1000,2000):#1-499, 500-1000, 1000-2000, >20000
            p3+=1
        elif temp in range(2000,5000):
            p4+=1
        else:
            p5+=1
    return p1,p2,p3,p4,p5