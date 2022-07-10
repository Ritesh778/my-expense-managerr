import sqlite3 as sq
from matplotlib import dates

conn = sq.connect('database.db',check_same_thread=False)
c = conn.cursor()

def create_user_record():
    #Connecting to sqlite
    conn = sq.connect('user_record.db')

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Creating table as per requirement
    sql ='''CREATE TABLE USERS(
    RANDOM_USERNAME CHAR(20) NOT NULL,
    uNAME CHAR(20) NOT NULL,
    USERNAME CHAR(20) NOT NULL,
    USER_EMAIL CHAR(20),
    PASS_WORD CHAR(20) NOT NULL
    )'''

    cursor.execute(sql)
    conn.commit()
    conn.close()
    
    
    
def create_newuser(RANDOM_USERNAME,uNAME,USERNAME,USER_EMAIL,PASS_WORD):
    conn = sq.connect('user_record.db')
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO USERS(RANDOM_USERNAME,uNAME,USERNAME, USER_EMAIL, PASS_WORD) VALUES (?,?,?, ?, ?)',(RANDOM_USERNAME,uNAME,USERNAME, USER_EMAIL, PASS_WORD))
    conn.commit()
    conn.close()


def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS personal_expense(username TEXT,date DATE,details TEXT,remark TEXT,credit TEXT,debit TEXT,total TEXT)')


def add_data(username,date,details,remark,credit,debit,total):
	c.execute('INSERT INTO personal_expense(username,date,details,remark,credit,debit,total) VALUES (?,?,?,?,?,?,?)',(username,date,details,remark,credit,debit,total))
	conn.commit()


def view_all_data(username):
	c.execute('SELECT * FROM personal_expense WHERE username="{}"'.format(username))
	data = c.fetchall()
	return data

def view_all_dates(username):
	c.execute('SELECT DISTINCT date FROM personal_expense WHERE username="{}"'.format(username))
	data = c.fetchall()
	return data

def view_all_details(username):
	c.execute('SELECT DISTINCT details FROM personal_expense WHERE username="{}"'.format(username))
	data = c.fetchall()
	return data

def get_date(username,date):
	c.execute('SELECT * FROM personal_expense WHERE username="{}" and date="{}" '.format(username,date))
	data = c.fetchall()
	return data

def edit_task_data(new_date,new_details,new_remark,new_credit,new_debit,new_total,username,date,details,remark,credit,debit,total):
	c.execute("UPDATE personal_expense SET date =?,details=?,remark=?,credit=?,debit=?,total=? WHERE username=? and date=? and details=? and remark=? and credit=? and debit=? and total=? ",(new_date,new_details,new_remark,new_credit,new_debit,new_total,username,date,details,remark,credit,debit,total))
	conn.commit()
	data = c.fetchall()
	return data

def delete_data(username,date,details):
	c.execute('DELETE FROM personal_expense WHERE username="{}" and date="{}" and details="{}"'.format(username,date,details))
	conn.commit()

