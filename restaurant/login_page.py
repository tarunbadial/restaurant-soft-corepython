from pymysql import *
from tkinter import *
from tkinter import messagebox as ms,ttk
from PIL import ImageTk, Image
import os
root=Tk()
def login():
	global user,passwd
	root.title("LOGIN")
	root.configure(background="#bfeb42")
	root.geometry("300x350+450+250")
	root.iconbitmap('Long-Shadow.ico')
	canvas = Canvas(root,width = 160, height = 150)      
	canvas.place(x=70,y=5)      
	img = PhotoImage(file="Restaurant.png")      
	canvas.create_image(0,0,anchor=NW, image=img) 
	can=Label(root,text="TARUNA RESTAURANT",font=("Courier",15,'bold'),bg="#bfeb42",fg="red")
	can.place(x=50,y=160)
	n=Label(root,text="User : ",font=("bold",11),bg="#bfeb42")
	n.place(x=20,y=190)
	user=Entry(root)
	user.place(x=100,y=190)
	m=Label(root,text="Password : ",font=("bold",11),bg="#bfeb42")
	m.place(x=20,y=220)
	passwd=Entry(root,show="*")
	passwd.place(x=100,y=220)
	passwd.bind("<Return>",search)
	B = Button(root,text ="LOGIN",fg='white',width=100,height=30,bg='brown',command=search)
	logo=PhotoImage(file ="login.png")
	B.configure(image =logo,compound=LEFT)
	small_logo=logo.subsample(2,2)
	B.configure(image=small_logo)
	B.place(x=100,y=250)
	B.bind("<Return>",search)
	root.mainloop()
def search(*event):
	try:	
		con=connect(db="restaurant",user="root",password="root",host="localhost")
		cur=con.cursor()
		cur.execute("select password from login  where name='%s'"%(user.get()))
		password=cur.fetchall()
		if(password[0][0]==passwd.get()):
			ms.showinfo("Congrats!!","You have Login Sucessfull")
			root.destroy()
			os.system('py user.py')
		else:
			ms.showinfo("Aborted!!","Login Unsucessfull")
			con.commit()
			con.close()
	except:
			ms.showinfo("Warning!","You Are Unauthrized User or you have enter wrong password")
			con.commit()
			con.close()
login()
root.mainloop()