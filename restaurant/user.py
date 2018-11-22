from tkinter import *
from tkinter import messagebox as ms
from os import getcwd,chdir,system
from tkinter import filedialog
from tkinter import scrolledtext
import time
import re
class Course():
	global d,nam,st,customer
	def customer(*event):
		global d,st
		chdir("customer")
		st=(nam.get())+".txt"
		d=open(st,'a')
		d.write("\n\nCustomer Serial No : "+str(num.get()))
		d.write("\nCustomer Name : "+nam.get())
		d.write("\nCustomer Address : "+addr.get())
		d.write("\nCustomer Mobile No : "+str(mob.get()))
		d.write("\nCustomer Table No : "+str(table1.get()))
		d.write("\nCustomer Entry Time : "+str(tim))
		d.write("\n..........................................")
		d.close()
		Course().main()	
	def User(self):
		global tim,nam,num,addr,table1,mob
		user=Tk()
		user.title("USER CREARTION")
		user.geometry("550x300+200+50")
		user.configure(background="#FFFF66")
		user.iconbitmap('Long-Shadow.ico')
		canvas = Canvas(user, width = 160, height = 150)      
		canvas.place(x=330,y=20)      
		img = PhotoImage(file="Restaurant.png")      
		canvas.create_image(0,0, anchor=NW, image=img) 
		can=Label(user,text="TARUNA RESTAURANT",font=("Courier",15,'bold'),bg="#FFFF66",fg="red")
		can.place(x=305,y=190)
		n=Label(user,text=" Customer Number : ",font=("bold",10),bg="#FFFF66")
		n.place(x=10,y=30)
		num=Entry(user)
		num.place(x=150,y=30)
		na=Label(user,text="Customer Name : ",font=("bold",10),bg="#FFFF66")
		na.place(x=10,y=60)
		nam=Entry(user)
		nam.place(x=150,y=60)
		address=Label(user,text="Address : ",font=("bold",10),bg="#FFFF66")
		address.place(x=10,y=90)
		addr=Entry(user)
		addr.place(x=150,y=90)
		mobile=Label(user,text="Mobile Number : ",font=("bold",10),bg="#FFFF66")
		mobile.place(x=10,y=120)
		mob=Entry(user)
		mob.place(x=150,y=120)
		table=Label(user,text="Table Number : ",font=("bold",10),bg="#FFFF66")
		table.place(x=10,y=150)
		table1=Entry(user)
		table1.place(x=150,y=150)
		tim=time.ctime()
		submit = Button(text ="CREATE",fg='white',width=100,height=20,bg='green',command=customer)
		logo=PhotoImage(file ="user.png")
		submit.configure(image =logo,compound=LEFT)
		small_logo=logo.subsample(2,2)
		submit.configure(image=small_logo)
		submit.place(x=100,y=190)
		submit.bind("<Return>",customer)
		user.mainloop()
	def main(self):
		main=Tk()
		main.title("COURSE OF HOTEL")
		main.geometry("450x900+200+50")     
		#main.iconbitmap('Long-Shadow.ico')
		main.configure(background="#bfeb42")
		l=Label(main, text="SELECT THE ITEM UNDER THE COURSE",fg="red",font=("bold",15),bg="#bfeb42")
		l.place(x=20,y=10)
#1Drinks
		tkvar = StringVar(main)
		choices = { "Jeera Pani.....................RS40","Masaledar Chhas................RS50","Taaze Phal Ka Ras..............RS80","Phaldari chaat................RS150"}
		tkvar.set('Jeera Pani                                                       RS40') # set the default option
		popupMenu = OptionMenu(main, tkvar, *choices)
		l2=Label(main, text="1.For Drinks & Cold Drinks",fg="black",font=("bold",10),bg="#bfeb42")
		l2.place(x=10,y=50)
		popupMenu.place(x=20,y=70)
		def change_dropdown(*args):
			#print(getcwd())
			print(tkvar.get())
			d=open(st,'a')
			d.write("\n"+tkvar.get())
			d.close()
		tkvar.trace('w', change_dropdown)

#2shorba
		tkvar2 = StringVar(main)
		choices2 = {"Jehangiri Shorba.............RS150","Tamatar Shorba...............RS130","Dakshini Dal Shorba...........RS120","Palak Shorba..................RS180","Cream Of Almond’s..............RS250"}
		tkvar2.set('Jehangiri Shorba                                      RS150') # set the default option
		popupMenu2 = OptionMenu(main, tkvar2, *choices2)
		l2=Label(main, text="2.For SHORBE(Soups)",fg="black",font=("bold",10),bg="#bfeb42")
		l2.place(x=10,y=100)
		popupMenu2.place(x=20,y=120)
		def change_dropdown(*args):
			print(tkvar2.get())
			d=open(st,'a')
			d.write("\n"+tkvar2.get())
			d.close()
		tkvar2.trace('w', change_dropdown)
	
#3for us paar se(Stater)	
		tkvar3 = StringVar(main)
		choices3 = {"Baked Bean On Toast............RS100","Paneer Fritters...............RS150","Cheese Chilly Toast...........RS160","Corn Pakoda..................RS180"}
		tkvar3.set('Baked Bean On Toast                                   RS100') # set the default option
		popupMenu3 = OptionMenu(main, tkvar3 ,*choices3)
		l3=Label(main, text="3.For US PAAR SE(From The Continent{Starters}",fg="black",font=("bold",10),bg="#bfeb42")
		l3.place(x=10,y=150)
		popupMenu3.place(x=20,y=170)
		def change_dropdown(*args):
			print(tkvar3.get())
			d=open(st,'a')
			d.write("\n"+tkvar3.get())
			d.close()
		tkvar3.trace('w', change_dropdown)
		
#4 tandor
		tkvar4 = StringVar(main)
		choices4 = {"Murgh Adraki Kebab............Rs.300","Murgh Tandoori................Rs.350","Mumtaz Tangdi ( 3 Pieces)....Rs.400","Murgh Mohini Seekh...........Rs.350","Angaara Kebab................Rs.450","Kalimiri Kebab...............Rs.500","Chilli Milli Kebab...........Rs.400","Malai Seekh Dilbahar.........Rs.450","Boti Kebab...................Rs.360","Kebab – E – Gulistan.........Rs.350","Macchi Amritsari Tikka.......Rs.150","Jhinga Nizami................Rs.160","Hara Bhara Kebab.............Rs.150","Sabizi Hariyali Seekh........Rs.150"}
		tkvar4.set('Murgh Adraki Kebab                                   Rs.300') # set the default option
		popupMenu4 = OptionMenu(main, tkvar4 ,*choices4)
		l4=Label(main, text="4.For AATISH –E- TANDOOR(From Our Clay Oven)",fg="black",font=("bold",10),bg="#bfeb42")
		l4.place(x=10,y=200)
		popupMenu4.place(x=20,y=220)
		def change_dropdown(*args):
			print(tkvar4.get())
			d=open(st,'a')
			d.write("\n"+tkvar4.get())
			d.close()
		tkvar4.trace('w', change_dropdown)
		
		#5
		tkvar5 = StringVar(main)
		choices5 = {"Spring chickencookedtomatogravy………………………RS150","Grilled chicken with poundedmasala……………………………RS150","tender chicken bedrice with mild sauce………………………RS150","spring chicken mixsesame&coconut………....…RS110","Tender spring chicken…………RS160","Butter chicken in a tantalizing gravy…………………RS140","Boneless sauteed with abundance of ginger&IS…………………..RS110"}
		tkvar5.set('Murgh Adraki Kebab                                     Rs.300') # set the default option
		popupMenu5 = OptionMenu(main, tkvar5 ,*choices5)
		l5=Label(main, text="5.For MURG-E-LAZAKET(The Spring Chicken)",fg="black",font=("bold",10),bg="#bfeb42")
		l5.place(x=10,y=250)
		popupMenu5.place(x=20,y=270)
		def change_dropdown(*args):
			print(tkvar5.get())
			d=open(st,'a')
			d.write("\n"+tkvar5.get())
			d.close()
		tkvar5.trace('w', change_dropdown)
		#6 ghosh
		tkvar6 = StringVar(main)
		choices6 ={"Bhuna Gosht……………………………………………RS120","Roganjosh…………………………………………………..RS420","Gosht Kadai Masala………………………………RS350","Tawa Gosht………………………………………………..RS500","Gosht Hara Masala……………………………….RS600","Mutton Peshawari……………………………………RS500","Mutton Saagwala………………………………………RS500"}
		tkvar6.set('Bhuna Gosht                                                RS120') # set the default option
		popupMenu6 = OptionMenu(main,tkvar6 ,*choices6)
		l6=Label(main, text="6.for GOSHT – E – BAHARAN(Lamb From The Chef’s Pan)",fg="black",font=("bold",10),bg="#bfeb42")
		l6.place(x=10,y=300)
		popupMenu6.place(x=20,y=320)
		def change_dropdown(*args):
			print(tkvar6.get())
			d=open(st,'a')
			d.write("\n"+tkvar6.get())
			d.close()
		tkvar6.trace('w', change_dropdown)
		#total working
		def final_bill(*event):
			fin=[]
			d=open(st,'r+')
			a=d.readlines()[9:]
			for x in a:
				m=re.findall(r'\d',x) 
				h=''.join(m)
				if(h.isdigit()):	
					fin.append(int(h))		
			print(fin)
			d.write("\nTotal ........................."+str(sum(fin)))
			d.close()
		def final_tk(*self):
			final_fg=Tk()
			final_fg.title("BILL(CASH MEMO)")
			final_fg.geometry("350x400+200+50")
			final_fg.configure(background="white")
			#final.iconbitmap('Long-Shadow.ico')
		#	canv = Canvas(final, width = 160, height = 150)      
		#	canv.place(x=100,y=20)      
		#	img = PhotoImage(file="Restaurant.png")      
		#	canv.create_image(0,0, anchor=NW, image=img) 
			d=open(st,'r')
			a=d.read()
			lf=Label(final_fg, text=a,fg="black",font=("bold",10),bg="#FFFF66")
			lf.place(x=10,y=100)
			d.close()
			final_fg.mainloop()
		final_sub = Button(main,text ="FINAL SUBMIT",fg='black',bg='green',command=final_bill,font=("bold",10))#,width=150,height=15
		final_sub.place(x=100,y=390)
		final_sub.bind("<Return>",final_bill)
		bill=Button(main,text ="Bill",fg='white',bg='green',width=8,height=1,command=final_tk,font=("bold",10))
		bill.place(x=250,y=390)
		main.mainloop()		
		
	
c=Course()
c.User()
#c.main()
