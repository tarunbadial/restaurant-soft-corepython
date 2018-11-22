from tkinter import *
from tkinter import messagebox as ms
from os import getcwd,chdir,system
from tkinter import filedialog
from tkinter import scrolledtext
from PIL import ImageTk, Image
import re
from user import st
class Main:	
	def main(self):
		main=Tk()
		main.title("COURSE OF HOTEL")
		main.geometry("450x900+200+50")     
		main.iconbitmap('Long-Shadow.ico')
		main.configure(background="#bfeb42")
		path = "hd.jpg"
		img = ImageTk.PhotoImage(Image.open(path))
		panel = Label(main, image = img)
		panel.pack(side = "bottom", fill = "both", expand = "yes")
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
			print(getcwd())
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
		choices4 = {"Murgh Adraki Kebab............Rs.300","Murgh Tandoori................Rs.350","Mumtaz Tangdi ( three Pieces)....Rs.400","Murgh Mohini Seekh...........Rs.350","Angaara Kebab................Rs.450","Kalimiri Kebab...............Rs.500","Chilli Milli Kebab...........Rs.400","Malai Seekh Dilbahar.........Rs.450","Boti Kebab...................Rs.360","Kebab – E – Gulistan.........Rs.350","Macchi Amritsari Tikka.......Rs.150","Jhinga Nizami................Rs.160","Hara Bhara Kebab.............Rs.150","Sabizi Hariyali Seekh........Rs.150"}
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
		
#5- Chicken
		tkvar5 = StringVar(main)
		choices5 = {"Spring chickencookedtomatogravy………………………RS150","Grilled chicken with poundedmasala……………………………RS150","tender chicken bedrice with mild sauce………………………RS150","spring chicken mixsesame&coconut………....…RS110","Tender spring chicken…………RS160","Butter chicken in a tantalizing gravy…………………RS140","Boneless sauteed with abundance of ginger&IS…………………..RS110"}
		tkvar5.set('Spring chickencookedtomatogravy………………………RS150') # set the default option
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
			final=Tk()
			final.title("BILL(CASH MEMO)")
			final.geometry("350x600+200+50")
			final.configure(background="#bfeb42")
			final.iconbitmap('Long-Shadow.ico')
			#canv = Canvas(final, width = 160, height = 150)      
			#canv.place(x=100,y=20)      
			#img = PhotoImage(file="Restaurant.png")      
			#canv.create_image(0,0, anchor=NW, image=img) 
			d=open(st,'r')
			a=d.read()
			lf=Label(final, text=a,fg="black",font=("bold",10),bg="#bfeb42")
			lf.place(x=10,y=210)
			d.close()
			final.mainloop()
		final_sub = Button(main,text ="FINAL SUBMIT",fg='black',bg='green',command=final_bill,font=("bold",10))#,width=150,height=15
		final_sub.place(x=100,y=390)
		final_sub.bind("<Return>",final_bill)
		bill=Button(main,text ="Bill",fg='white',bg='green',width=80,height=20,command=final_tk,font=("bold",10))
		logo=PhotoImage(file ="bill.png")
		bill.configure(image =logo,compound=LEFT)
		small_logo=logo.subsample(2,2)
		bill.configure(image=small_logo)
		
		bill.place(x=250,y=390)
		main.mainloop()		
m=Main()
m.main()