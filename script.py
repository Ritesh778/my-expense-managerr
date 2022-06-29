import sqlite3 as sq
from matplotlib import dates

conn = sq.connect('database.db',check_same_thread=False)
c = conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS personal_expense(date DATE,details TEXT,remark TEXT,credit TEXT,debit TEXT,total TEXT)')


def add_data(date,details,remark,credit,debit,total):
	c.execute('INSERT INTO personal_expense(date,details,remark,credit,debit,total) VALUES (?,?,?,?,?,?)',(date,details,remark,credit,debit,total))
	conn.commit()


def view_all_data():
	c.execute('SELECT * FROM personal_expense')
	data = c.fetchall()
	return data

def view_all_dates():
	c.execute('SELECT DISTINCT date FROM personal_expense')
	data = c.fetchall()
	return data

def view_all_details():
	c.execute('SELECT DISTINCT details FROM personal_expense')
	data = c.fetchall()
	return data

def get_date(date):
	c.execute('SELECT * FROM personal_expense WHERE date="{}"'.format(date))
	data = c.fetchall()
	return data

def edit_task_data(new_date,new_details,new_remark,new_credit,new_debit,new_total,date,details,remark,credit,debit,total):
	c.execute("UPDATE personal_expense SET date =?,details=?,remark=?,credit=?,debit=?,total=? WHERE date=? and details=? and remark=? and credit=? and debit=? and total=? ",(new_date,new_details,new_remark,new_credit,new_debit,new_total,date,details,remark,credit,debit,total))
	conn.commit()
	data = c.fetchall()
	return data

def delete_data(date,details):
	c.execute('DELETE FROM personal_expense WHERE date="{}" and details="{}"'.format(date,details))
	conn.commit()