from pymysql import*
from os import getcwd,chdir
import time
list=[]
class Login:
	def get1(self):
		self.user=input("enter the user name : ")
		self.password=input("enter the password : ")
	def search(self):
		try:	
			con=connect(db="restaurant",user="root",password="root",host="localhost")
			cur=con.cursor()
			cur.execute("select password from login  where name='%s'"%self.user)	
			password=cur.fetchall()
			if(password[0][0]==self.password):
				print("Login,logged in sucessfull")
				s.get()
				s.table_sit()
				s.display()
			else:
				print("Login,logged in unsucessfull")
				con.commit()
				con.close()
		except:
			print("You Are Unauthrized user and wrong value enter")
class Gateenter(Login):
	def get(self):
		self.srno=int(input("Enter the Customer Number : "))
		self.name=input("Enter the customer name : ")
		self.address=input("Enter the Customer Address : ")
		self.mobile=int(input("Enter the Mobile Number : "))
		self.table=int(input("Allocate the table Number : "))
		self.time=time.ctime()
		chdir("customer")
		print(getcwd())
		self.st=self.name+".txt"
		print(self.st)
		self.d=open(self.st,'a')
		self.d.write("\n\nCustomer Serial No : "+str(self.srno))
		self.d.write("\nCustomer Name : "+self.name)
		self.d.write("\nCustomer Address : "+self.address)
		self.d.write("\nCustomer Mobile No : "+str(self.mobile))
		self.d.write("\nCustomer Table No : "+str(self.table))
		self.d.write("\nCustomer Entry Time : "+str(self.time))
		self.d.write("\n..........................................................")			
	def display(self):
		a=open(self.st,"r")
		print(a.read())
		a.close()
class Table(Gateenter,Login):
		def table_sit(self):
			while True:	
				print("----------welcome on table number",self.table,"----------------")
				print("Select The Following choices")
				print("1.For Drinks & Cold Drinks")
				print("2.For SHORBE(Soups)")
				print("3.For US PAAR SE(From The Continent{Starters})")
				print("4.For AATISH –E- TANDOOR(From Our Clay Oven)")
				print("5.For MURG-E-LAZAKET(The Spring Chicken)")
				print("6.for GOSHT – E – BAHARAN(Lamb From The Chef’s Pan)")
				print("7.SAMUNDARI ZEWAR(Jewels Of The Deep Sea)")
				print("8.SABZI HARIYALI(Garden Fresh Vegetables)")
				print("9.LAZZAT – E – BASMATI(Pearl Of The Kitchen)")
				print("10.LUQMAAT – E – ROTI(Indian Bread)")
				print("11.MEETHE SAPNE(Sweet Sensations)")
				print("12.SAMNUDAR PAAR KE MEETHE SAPNE(Continental Desserts)")
				print("13.CHINESE MENU THAUPOON(Starters)")
				print("14.TAIPAN(Sizzlers)")
				print("15.THEEM PAAN(Desserts)")
				print("16.For Exit")
				choice=int(input("Enter the Course : "))
				print(choice)
				if (choice==1):
					g=open("F:/Python/ducat/project/Restaurant/drinks.txt","r")
					print(g.read())
					g.close()
					while True:
						print("1.Jeera Pani....RS40")
						print("2.Masaledar Chhas....RS50")
						print("3.Taaze Phal Ka Ras..RS80")
						print("4.Phaldari chaat...RS150")
						print("5.For Previous List")
						r=int(input("Enter your drink code : "))
						if(r==1):
							self.d.write("\nJeera Pani..................... 40")
							list.append(40)
						elif(r==2):
							self.d.write("\nMasaledar Chhas................. 50")
							list.append(50)
						elif(r==3):
							self.d.write("\nTaaze Phal Ka Ras................ 80")
							list.append(80)
						elif(r==4):
							self.d.write("\nPhaldari chaat....................150")
							list.append(150)
						elif(r==5):
							print("you have Sucessfull return to perivious list")
							break
				elif(choice==2):
					n=open("F:/Python/ducat/project/Restaurant//soups.txt","r")
					print(n.read())
					n.close()
					while True:
						print("1.Jehangiri Shorba...RS150")
						print("2.Tamatar Shorba....RS130")
						print("3.Dakshini Dal Shorba....RS120")
						print("4.Palak Shorba.....RS180")
						print("5.Cream Of Almond’s.....RS250")
						print("6.For Previous List")
						t=int(input("Enter the soup code"))
						if(t==1):
							self.d.write("\nJehangiri Shorba...................... 150")
							list.append(150)
						elif(t==2):
							self.d.write("\nTamatar Shorba.........................130")
							list.append(130)
						elif(t==3):
							self.d.write("\nDakshini Dal Shorba.....................120")
							list.append(120)
						elif(t==4):
							self.d.write("\nPalak Shorba............................. 180")
							list.append(180)
						elif(t==5):
							self.d.write("\nCream Of Almond’s......................... 250")
							list.append(250)
						elif(t==6):
							print("you have Sucessfull return to perivious list")
							break
				elif(choice==3):
					n=open("F:/Python/ducat/project/Restaurant//stater.txt","r")
					print(n.read())
					n.close()
					while True:
						print("1.Baked Bean On Toast..RS100")
						print("2.Paneer Fritters......RS150")
						print("3.Cheese Chilly Toast...RS160")
						print("4.Corn Pakoda...........RS180")
						print("5.For Previous List")
						r=int(input("Enter the stater code : "))
						if(r==1):
							self.d.write("\nBaked Bean On Toast...................100")
							list.append(100)
						elif(r==2):
							self.d.write("\nPaneer Fritters........................150")
							list.append(150)
						elif(r==3):
							self.d.write("\nCheese Chilly Toast....................160")
							list.append(160)
						elif(r==4):
							self.d.write("\nCorn Pakoda............................180")
							list.append(180)
						elif(r==5):
							print("you have Sucessfull return to perivious list")
							break
				elif(choice==4):
					n=open("F:/Python/ducat/project/Restaurant/tandor.txt","r")
					print(n.read())
					n.close()
					while True:
						print("1.Murgh Adraki Kebab....Rs.300")
						print("2.Murgh Tandoori...Rs.350")
						print("3.Mumtaz Tangdi ( 3 Pieces)..Rs.400")
						print("4.Murgh Mohini Seekh........Rs.350")
						print("5.Angaara Kebab..............Rs.450")
						print("6.Kalimiri Kebab.............Rs.500")
						print("7.Chilli Milli Kebab.........Rs.400")
						print("8.Malai Seekh Dilbahar.......Rs.450")
						print("9.Boti Kebab.................Rs.360")
						print("10.Kebab – E – Gulistan......Rs.350")
						print("11.Macchi Amritsari Tikka.......Rs.150")
						print("12.Jhinga Nizami................Rs.160")
						print("13.Hara Bhara Kebab.............Rs.150")
						print("14.Sabizi Hariyali Seekh........Rs.150")
						print("15.For Previous List")
						t=int(input("Enter the tandoor dish code : "))
						if(t==1):
							self.d.write("\nMurgh Adraki Kebab...............300")
							list.append(300)
						elif(t==2):
							self.d.write("\nMurgh Tandoori...................350")
							list.append(350)
						elif(t==3):
							self.d.write("\nMumtaz Tangdi ( 3 Pieces).........400")
							list.append(400)
						elif(t==4):
							self.d.write("\nMurgh Mohini Seekh................350")
							list.append(350)
						elif(t==5):					
							self.d.write("\nAngaara Kebab..........................450")
							list.append(450)
						elif(t==6):
							self.d.write("\nKalimiri Kebab........................500")
							list.append(500)
						elif(t==7):
							self.d.write("\nChilli Milli Kebab.......................400")
							list.append(400)
						elif(t==8):
							self.d.write("\nMalai Seekh Dilbahar......................450")
							list.append(450)
						elif(t==9):
							self.d.write("\nBoti Kebab................................360")
							list.append(360)
						elif(t==10):
							self.d.write("\nKebab – E – Gulistan......................350")
							list.append(350)
						elif(t==11):
							self.d.write("\nMacchi Amritsari Tikka....................150")
							list.append(150)
						elif(t==12):
							self.d.write("\nJhinga Nizami.............................160")
							list.append(160)
						elif(t==13):
							self.d.write("\nHara Bhara Kebab.............................150")
							list.append(150)
						elif(t==14):
							self.d.write("\nSabizi Hariyali Seekh.......................150")
							list.append(150)
						elif(t==15):
							print("you have Sucessfull return to perivious list")
							break
				elif(choice==5):
					n=open("F:/Python/ducat/project/Restaurant/chicken.txt","r")
					print(n.read())
					n.close()
					while True:
						print("1.Murgh Mumtaz………….RS150")
						print("2.Murgh Karachi…………RS150")
						print("3.Reshmi Chello……..RS150")
						print("4.Murgh Hyderabadi…RS110")
						print("5.Murgh Kothmiri………RS160")
						print("6.Murgh Makhani…………RS140")
						print("7.Methi Murgh………………RS110")
						print("8.For Previous List")
						v=int(input("Enter the Chicken code : "))
						if(v==1):
							self.d.write("\nMurgh Mumtaz…………......................RS150")
							list.append(150)
						elif(v==2):	
							self.d.write("\nMurgh Karachi……….....................…RS150")
							list.append(150)
						elif(v==3):
							self.d.write("\nReshmi Chello…….......................RS150")
							list.append(150)
						elif(v==4):
							self.d.write("\nMurgh Hyderabadi.....................…RS110")
							list.append(110)
						elif(v==5):
							self.d.write("\nMurgh Kothmiri……….....................RS160")
							list.append(160)
						elif(v==6):
							self.d.write("\nMurgh Makhani……….....................…RS140")
							list.append(140)
						elif(v==7):
							self.d.write("\nMethi Murgh……………….....................RS110")
							list.append(110)
						elif(v==8):
							print("you have Sucessfull return to perivious list")
							break
				elif(choice==6):
					n=open("F:/Python/ducat/project/Restaurant/ghosh.txt","r")
					print(n.read())
					n.close()
					while True:
						print("1.Bhuna Gosht….RS120")
						print("2.Roganjosh...RS420")
						print("3.Gosht Kadai Masala….RS350")
						print("4.Tawa Gosht…..RS500")
						print("5.Gosht Hara Masala….RS600")
						print("6.Mutton Peshawari…..RS500")
						print("7.Mutton Saagwala……RS500")
						print("8.For Previous List")
						r=int(input("Enter the ghosh code : "))
						if(r==1):
							self.d.write("\nBhuna Gosht…..........................120")
							list.append(120)
						elif(r==2):
							self.d.write("\nRoganjosh.............................420")
							list.append(420)
						elif(r==3):
							self.d.write("\nGosht Kadai Masala…....................350")
							list.append(350)
						elif(r==4):
							self.d.write("\nTawa Gosht........................…....500")
							list.append(500)
							
						elif(r==5):
							self.d.write("\nGosht Hara Masala….....................600")
							list.append(600)
						elif(r==6):
							self.d.write("\nMutton Peshawari…......................500")
							list.append(500)
						elif(r==7):
							self.d.write("\nMutton Saagwala……......................500")
							list.append(500)
						elif(r==8):
							print("you have Sucessfull return to perivious list")
							break	
				elif(choice==7):
					n=open("F:/Python/ducat/project/Restaurant/samundari.txt","r")
					print(n.read())
					n.close()	
					while True:
						print("1.Dakshini Machhi Curry………….RS600")
						print("2.Pudina Machhi....…………………….RS500")
						print("3.Kadai Jhinga……………………………………RS450")
						print("4.Aap Ki Pasand Ka Kekra/Lobster/Tiger Prawns……RS600")
						print("5.Jhinga / Fish Koliwada…………RS450")
						print("6.Fish Goan Curry……………………………RS300")
						print("7.Tawa Fish……………………………………………RS400")
						print("8.For Previous List")
						d=int(input("Enter the Samundari dishes code : "))
						if(d==1):
							self.d.write("\nDakshini Machhi Curry…………...............600")
							list.append(600)
						elif(d==2):
							self.d.write("\nPudina Machhi...........................500")
							list.append(600)
						elif(d==3):
							self.d.write("\nKadai Jhinga……………………………………..............450")
							list.append(450)
						elif(d==4):
							self.d.write("\nAap Ki Pasand Ka Kekra/Lobster/Tiger Prawns……600")
							list.append(600)
						elif(d==5):
							self.d.write("\nJhinga / Fish Koliwada………….................450")
							list.append(450)
						elif(d==6):
							self.d.write("\nFish Goan Curry…………………………….................300")
							list.append(300)
						elif(d==7):
							self.d.write("\nTawa Fish……………………………………………...............400")
							list.append(400)	
						elif(d==8):
							print("you have Sucessfull return to perivious list")
							break	
				elif(choice==8):
					n=open("	F:/Python/ducat/project/Restaurant/vegitable.txt","r")
					print(n.read())
					n.close()
					while True:
						print("1.Makhmali Kofta.............……………………………………………………………………………………………...........RS100")
						print("2.Kaju Dhingri Mutter……………………...........………………………………………………………………………........RS200")
						print("3.Hara Makai Sabzi…………………………………………………………...........……………………………………….........RS100")
						print("4.Navrattan Korma…………………………………………………………………………………………..........…………….......….RS200")
						print("5.Dum Aloo Kashmiri……………………………………………………………………………………………………..................RS150")
						print("6.Sabzi Ka Saag……………………………………………………………………………………………………….....................RS200")
						print("7.Sarson Ka Saag……………………………………………………………………………………………………....................…RS250")
						print("8.Sabzi Baby Corn Jalfrezi…………………………………………………………………………………………………............RS150")
						print("9.Bhindi Do Pyaza / Dahi Bhindi……………………………………………………………………………………………........RS100")
						print("10.Pakoda Kadi………………………………………………………………………………………………………………...................……RS80")
						print("11.Methi Malai Mutter………………………………………………………………………………………………...................RS150")
						print("12.Paneer Makhani Ki Boti…………………………………………………………………………………………………..............RS100")
						print("13. for previous list")
						g=int(input("Enter the code of vegitable: "))
						if(g==1):
							self.d.write("Makhmali Kofta.............……………………………………...........RS100")
							list.append(100)
						elif(g==2):
							self.d.write("Kaju Dhingri Mutter…………………………………………………………………........RS200")
							list.append(200)
						elif(g==3):
							self.d.write("Hara Makai Sabzi……………………………………………………………………….........RS100")
							list.append(100)
						elif(g==4):
							self.d.write("Navrattan Korma………………………………………………………………………….......….RS200")
							list.append(200)
						elif(g==5):
							self.d.write("Dum Aloo Kashmiri……………………………………………………………………………………………RS150")
							list.append(150)
						elif(g==6):
							self.d.write("Sabzi Ka Saag………………………………………………………………………………………………………RS200")
							list.append(200)
						elif(g==7):
							self.d.write("Sarson Ka Saag……………………………………………………………………………………………………RS250")
							list.append(250)
						elif(g==8):
							self.d.write("Sabzi Baby Corn Jalfrezi………………………………………………………………………….RS150")
							list.append(150)
						elif(g==9):
							self.d.write("Bhindi Do Pyaza / Dahi Bhindi…………………………………………………………….RS100")
							list.append(100)
						elif(g==10):
							self.d.write("Pakoda Kadi…………………………………………………………………………………………………………………RS80")
							list.append(80)
						elif(g==11):
							self.d.write("Methi Malai Mutter………………………………………………………………………………………….RS150")
							list.append(150)
						elif(g==12):
							self.d.write("Paneer Makhani Ki Boti……………………………………………………………………………….RS100")
							list.append(100)
						elif(g==13):
							print("you have Sucessfull return to perivious list")
							break
				elif(choice==9):
					n=open("F:/Python/ducat/project/Restaurant/basmati.txt","r")
					print(n.read())
					n.close()
					'''while True:
					
						elif(g==13):
							print("you have Sucessfull return to perivious list")
							break'''
					print("LAZZAT – E – BASMATI(Pearl Of The Kitchen)")
				elif(choice==10):
					n=open("F:/Python/ducat/project/Restaurant/roti.txt","r")
					print(n.read())
					n.close()
					'''while True:
						elif(g==13):
							print("you have Sucessfull return to perivious list")
							break'''
					print("LUQMAAT – E – ROTI(Indian Bread)")
				elif(choice==11):
					n=open("F:/Python/ducat/project/Restaurant/sweets.txt","r")
					print(n.read())
					n.close()
					'''while True:
						elif(g==13):
							print("you have Sucessfull return to perivious list")
							break'''
					print("MEETHE SAPNE(Sweet Sensations)")
				elif(choice==12):
					n=open("F:/Python/ducat/project/Restaurant/samunder sweets.txt","r")
					print(n.read())
					n.close()
					'''while True:
						elif(g==13):
							print("you have Sucessfull return to perivious list")
							break'''
					print("SAMNUDAR PAAR KE MEETHE SAPNE(Continental Desserts)")
				elif(choice==13):
					n=open("F:/Python/ducat/project/Restaurant/chiense.txt","r")
					print(n.read())
					n.close()
					'''while True:
						elif(g==13):
							print("you have Sucessfull return to perivious list")
							break'''
					print("CHINESE MENU THAUPOON(Starters)")
				elif(choice==14):
					n=open("F:/Python/ducat/project/Restaurant/tipan.txt","r")
					print(n.read())
					n.close()
					'''while True:
						elif(g==13):
							print("you have Sucessfull return to perivious list")
							break'''
					print("TAIPAN(Sizzlers)")
				elif(choice==15):
					n=open("F:/Python/ducat/project/Restaurant/desserts.txt","r")
					print(n.read())
					n.close()
					'''while True:
						elif(g==13):
							print("you have Sucessfull return to perivious list")
							break'''
					print("THEEM PAAN(Desserts)")
				elif(choice==16):
					print("you have Sucessfull exit")
					self.d.write("\nTOTAL....................................RS"+str(sum(list)))
					self.d.close()
					break

s=Table()
s.get1()
s.search()	
input()