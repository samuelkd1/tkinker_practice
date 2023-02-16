from tkinter import *
from PIL import ImageTk, Image
import sqlite3


root = Tk()
root.title("database stuff")
root.geometry("600x600")

# databases 
# create a database 
# this will create a connection 
conn = sqlite3.connect("address_book.db")
# cursor makes changes for you
cursor = conn.cursor()

# table only need to create once
''' 
cursor.execute("""CREATE TABLE addresses (
first_name TEXT,
last_name TEXT,
address TEXT,
city TEXT,
state TEXT,
zipcode INT


    )

 """)
'''

# creating an submit function for database

def submit():
	# some code to actually submit the stuff
	# we need a connection within the function

	# note, make these the same
	conn = sqlite3.connect("address_book.db")

	# ...and cursor
	cursor = conn.cursor()

	record_id = delete_box.get()
	#insert into table
	cursor.execute("INSERT INTO addresses VALUES (:f_name,:l_name,:address, :city, :state, :zipcode)",

		{
		'f_name': f_name.get(),
		'l_name': l_name.get(),
		'address': address.get(),
		'city': city.get(),
		'state': state.get(),
		'zipcode': zipcode.get(),

		'oid': record_id

		})

	# to save changes
	conn.commit()

	# to close connections
	conn.close()

	# clear Text Boxes so create an end
	f_name.delete(0, END)
	l_name.delete(0, END)
	address.delete(0,END)
	city.delete(0, END)
	state.delete(0, END)
	zipcode.delete(0, END)


# create query function
def query():

	# we need a connection within the function
	conn = sqlite3.connect("address_book.db")

	# ...and cursor
	cursor = conn.cursor()

	#querying database
	cursor.execute("SELECT *, oid FROM addresses")
	records = cursor.fetchall()

	# lets create a 4 loop to get records
	# we need to make an empty string so we have a variable there

	print_records = " "

# you can manipulate to get specific parts record[0] will get first name.
	for record in records:
		print_records += f"{record[0]} {record[1]} \t{record[6]} \n"

	query_label = Label(root, text = print_records)
	query_label.grid(row = 8, column = 0, columnspan = 2)




	# to save changes
	conn.commit()

	# to close connections
	conn.close()

# create function to update a record (in a whole new window)
def update():
	# we need a connection within the function
	conn = sqlite3.connect("address_book.db")

	# ...and cursor
	cursor = conn.cursor()

	record_id = delete_box.get()

	cursor.execute(""" UPDATE addresses SET
		first_name = :first,
		last_name = :last,
		address = :address,
		city = :city,
		state = :state,
		zipcode = :zipcode

		WHERE oid = :oid""",


		{'first' : f_name_editor.get(),
		'last': l_name_editor.get(),
		'address': address_editor.get(),
		'city': city_editor.get(),
		'state': state_editor.get(),
		'zipcode': zipcode_editor.get(),
		'oid': record_id
		})

	# to save 
	conn.commit()

	# to close connections
	conn.close()

	editor.destroy()


def edit():
	global editor
	editor = Tk()
	editor.title("update record")
	editor.geometry("400x250")


	# we need a connection within the function
	conn = sqlite3.connect("address_book.db")

	# ...and cursor
	cursor = conn.cursor()

	record_id = delete_box.get()
	#querying database
	cursor.execute("SELECT * FROM addresses WHERE oid = " + record_id)
	records = cursor.fetchall()

	# we need to make global as they carry over 2 functions
	global f_name_editor
	global l_name_editor
	global address_editor
	global city_editor
	global state_editor
	global zipcode_editor

	f_name_editor = Entry(editor, width = 30)
	f_name_editor.grid(row = 0, column = 1, padx = 20)

	l_name_editor = Entry(editor, width = 30)
	l_name_editor.grid(row = 1, column = 1, padx = 20)

	address_editor = Entry(editor, width = 30)
	address_editor.grid(row = 2, column = 1, padx = 20)

	city_editor = Entry(editor, width = 30)
	city_editor.grid(row = 3, column = 1)

	state_editor = Entry(editor, width = 30)
	state_editor.grid(row = 4, column = 1, padx = 20)

	zipcode_editor = Entry(editor, width = 30)
	zipcode_editor.grid(row = 5, column = 1, padx = 20)



	# create the labels for it 
	f_name_label = Label(editor, text = "First Name")
	f_name_label.grid(row = 0, column = 0)

	l_name_label = Label(editor, text = "Last Name")
	l_name_label.grid(row = 1, column = 0)

	address_label = Label(editor, text = "Address")
	address_label.grid(row = 2, column = 0)

	city_label = Label(editor, text = "City")
	city_label.grid(row = 3, column = 0)

	state_label = Label(editor, text = "State")
	state_label.grid(row = 4, column = 0)

	zipcode_label = Label(editor, text = "Zipcode")
	zipcode_label.grid(row = 5, column = 0)

	# loop through results
	for record in records:
		f_name_editor.insert(0,record[0])
		l_name_editor.insert(0,record[1])
		address_editor.insert(0,record[2])
		city_editor.insert(0,record[3])
		state_editor.insert(0,record[4])
		zipcode_editor.insert(0,record[5])
	

	# create a submit button to submit.
	# we need to create a new function to save this
	save_btn = Button(editor, text = "submit record", command = update)
	save_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx= 10, ipadx = 145)
	

	
	



 # create function to delete 

def delete():
	# we need a connection within the function
	conn = sqlite3.connect("address_book.db")

	# ...and cursor
	cursor = conn.cursor()


	cursor.execute("DELETE FROM addresses WHERE oid = " + delete_box.get())


	# to save 
	conn.commit()

	# to close connections
	conn.close()




# create an entry widget for each entry put in col one to sort out text next to it
f_name = Entry(root, width = 30)
f_name.grid(row = 0, column = 1, padx = 20)

l_name = Entry(root, width = 30)
l_name.grid(row = 1, column = 1, padx = 20)

address = Entry(root, width = 30)
address.grid(row = 2, column = 1, padx = 20)

city = Entry(root, width = 30)
city.grid(row = 3, column = 1)

state = Entry(root, width = 30)
state.grid(row = 4, column = 1, padx = 20)

zipcode = Entry(root, width = 30)
zipcode.grid(row = 5, column = 1, padx = 20)

# create box
delete_box = Entry(root, width = 30)
delete_box.grid(row = 9 ,column = 1)


# create the labels for it 
f_name_label = Label(root, text = "First Name")
f_name_label.grid(row = 0, column = 0)

l_name_label = Label(root, text = "Last Name")
l_name_label.grid(row = 1, column = 0)

address_label = Label(root, text = "Address")
address_label.grid(row = 2, column = 0)

city_label = Label(root, text = "City")
city_label.grid(row = 3, column = 0)

state_label = Label(root, text = "State")
state_label.grid(row = 4, column = 0)

zipcode_label = Label(root, text = "Zipcode")
zipcode_label.grid(row = 5, column = 0)

# create label

delete_box_label = Label(root, text = "Select ID")
delete_box_label.grid(row = 9, column = 0, columnspan = 1, pady = 10, padx = 10, ipadx = 13)


# now we need buttons to create 

submit_btn = Button(root, text = "Add record to Database", command = submit)
submit_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

# making a query button
query_btn = Button(root, text = " Show records", command = query)
query_btn.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx= 10, ipadx = 129)

# create a delete button 
delete_btn = Button(root, text = " Delete record", command = delete)
delete_btn.grid(row = 10, column = 0, columnspan = 2, pady = 10, padx= 10, ipadx = 137)

# create an update button
edit_btn = Button(root, text = "   Edit record   ", command = edit)
edit_btn.grid(row = 11, column = 0, columnspan = 3, pady = 10, padx= 10, ipadx = 140)




# to save changes
conn.commit()

# to close connections
conn.close()
root.mainloop() 