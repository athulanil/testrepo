import sqlite3

with sqlite3.connect('test.db') as db:
	c = db.cursor()

c.execute("CREATE TABLE IF NOT EXISTS data(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, descrip TEXT NOT NULL)")
db.commit()
db.close()

def add_data():
	try:
		with sqlite3.connect('test.db') as db:
			c = db.cursor()
		tit = raw_input("Enter the title: ")
		des = raw_input("Enter description: ")
		query = '''INSERT INTO data(title, descrip) VALUES('{title}', '{description}')'''
		formated_query = query.format(title=tit, description=des)
		c.execute(formated_query)
		print("Inserted")
		db.commit()
		db.close()
	    	
	except Exception as e:
		print(e)
		
def view_data():
	try:
		with sqlite3.connect('test.db') as db:
			c = db.cursor()
		c.execute('SELECT * FROM data')
		d = c.fetchall()
		for line in d:
			print(line)

	except Exception as e:
		print(e)

	finally:
		db.close()

def update_data():
	view_data()
	id = raw_input("Enter the ID to be updated: ")

	try:
		with sqlite3.connect('test.db') as db:
			c = db.cursor()
		new_title = raw_input("Enter new title: ")

		query = '''UPDATE data SET title='{}' WHERE id='{}' '''
		formated_query = query.format(new_title, id)
		c.execute(formated_query)
		db.commit()
		db.close()
		print("Updated")
	except Exception as e:
		raise e

def delete_data():
	view_data()
	id = raw_input("Enter the ID to be deleted: ")
	try:
		with sqlite3.connect('test.db') as db:
			c = db.cursor()
		query = '''DELETE FROM data WHERE id = '{}' '''
		formated_query = query.format(id)
		c.execute(formated_query)
		db.commit()
		db.close()
		print("Deleted")
	except Exception as e:
		print(e)

opt = ''
while opt != 'quit':
	print(' 1. Add Data \n 2. Update Data \n 3. Delete Data \n 4. View Data \n 5. quit')
	opt = int(input('Enter your choice: '))

	if opt == 1:
		add_data()

	elif opt == 2:
		update_data()

	elif opt == 3:
		delete_data()

	elif opt == 4:
		view_data()

	else:
		break
