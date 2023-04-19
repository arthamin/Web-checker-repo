from tkinter import *
import requests
import socket
import sys

root = Tk()
root.attributes('-fullscreen', False)
root.geometry("1920x1080")
root['bg']='#2e89c9'


def wwb():
	global menu, wwb, tutor, wrk

	frame_text_wwb = Frame(root, bg='#FFCC66')
	frame_text_wwb.place(relheight=1, relwidth=1)


	txt_wwb = Label(frame_text_wwb, text="Web-Checker: сайттар мен мақсатты хосттардың қосылу күйін тексеруге арналған бағдарлама", bg='#FFCC66', font='Impact 25')
	txt_wwb.place(relx=0.032, rely=0.25)

	frame_top_wwb = Frame(frame_text_wwb, bg = 'white', bd=5)
	frame_top_wwb.place(relheight=0.07, relwidth=1)

	txt_wwb = Label(frame_top_wwb, text='Сіздің «Web-checker» деген не?"', bg='white', font='Impact 50')
	txt_wwb.pack()

	txt2_wwb = Label(frame_text_wwb, text='Бағдарлама сіздің сүйікті сайтыңыздың неге ашылмағанын білуге ​​мүмкіндік береді', bg='#FFCC66', font='Impact 25')
	txt2_wwb.place(relx=0.13, rely=0.4)

	txt3_wwb = Label(frame_text_wwb, text='Немесе өзіңіздің веб-серверіңіз неге жұмыс істемейді!', bg='#FFCC66', font='Impact 25',)
	txt3_wwb.place(relx=0.22, rely=0.6)

	but1_wwb = Button(frame_text_wwb, text='Мәзірге оралу', bg='red', foreground='white', command=menu)
	but1_wwb['font']='Impact 20'
	but1_wwb.place(relx=0.45, rely=0.7)


	button_about = Button(frame_text_wwb, text='X', bg='red', foreground='Black', command=exit)
	button_about['font'] = 'Impact 30'
	button_about.place(relx=0.97, rely=0.0001, relheight=0.03, relwidth=0.03)



def menu():
	global menu, wwb, tutor, wrk

	frame_full_menu = Frame(root, bg='#FFCC66')
	frame_full_menu.place(relheight=1, relwidth=1)

	frame_top_menu = Frame(frame_full_menu, bg='white', )
	frame_top_menu.place(relheight=0.07, relwidth=1,)

	txt_menu = Label(frame_top_menu, text="Сәлеметсіз бе! Сіз қазір «Web-Checker» бағдарламасын пайдаланып жатырсыз!", bg='white', font='Impact 32')
	txt_menu.pack()



	but = Button(frame_full_menu, text='Сіздің «Web-checker» деген не?"', bg='red', foreground='white', command=wwb)
	but['font']='Impact 25'
	but.place(relx=0.29, rely=0.254, relwidth=0.4, relheight=0.06)

	but_menu = Button(frame_full_menu, text="«Web-Checker» пайдалану нұсқаулары", bg='red', foreground='white', command=tutor)
	but_menu['font']='Impact 23'
	but_menu.place(relx=0.29, rely=0.4, relheight=0.06, relwidth=0.4)

	but_menu1 = Button(frame_full_menu, text='Жұмысты бастау', bg='red', foreground='white', command=wrk)
	but_menu1['font']='Impact 25'
	but_menu1.place(relheight=0.06, relwidth=0.4, relx=0.29, rely=0.546)

	button_menu = Button(frame_full_menu, text='X', bg='red', foreground='Black', command=exit)
	button_menu['font'] = 'Impact 30'
	button_menu.place(relx=0.97, rely=0.0001, relheight=0.03, relwidth=0.03)



def tutor():
	global menu, wwb, tutor, wrk

	frame_full_tutor = Frame(root, bg='#FFCC66')
	frame_full_tutor.place(relheight=1, relwidth=1)

	frame_text_tutor = Frame(frame_full_tutor, bg='white',)
	frame_text_tutor.place(relheight=0.07, relwidth=1)

	txt_tutor = Label(frame_text_tutor, text='«Web-Checker» пайдалану нұсқаулары', bg='white', font='Impact 50')
	txt_tutor.pack()

	inst_tutor = Label(frame_full_tutor, text='Өтінішті қалай дұрыс енгізу керек?:', bg='#FFCC66', font='Impact 55')
	inst_tutor.place(relx=0.19, rely=0.18)

	inst_tutor2 = Label(frame_full_tutor, text='Бағдарламадан дұрыс жауап алу үшін барлық сұраулар осы пішінде болуы керек', bg='#FFCC66', font='Impact 25')
	inst_tutor2.place(relx=0.14, rely=0.40)

	inst_tutor3 = Label(frame_full_tutor, text='https://primer_URL.kz', bg='#FFCC66', font='Impact 50')
	inst_tutor3.place(relx=0.35, rely=0.60)

	but_tutor = Button(frame_full_tutor, text='Мәзірге оралу', bg='red', foreground='white', command=menu)
	but_tutor['font'] = 'Impact 20'
	but_tutor.place(relx=0.43, rely=0.75)


	button_tut = Button(frame_full_tutor, text='X', bg='red', foreground='Black', command=exit)
	button_tut['font'] = 'Impact 30'
	button_tut.place(relx=0.97, rely=0.0001, relheight=0.03, relwidth=0.03)



def wrk():
	global menu, wwb, tutor, wrk
	# Тут глобалим переменные,что бы check видел их корректно
	# Переменные глобалим выше самих переменных, иначе еррор
	global entry, var, frame_text_chk, frame_full_wrk 

	frame_full_wrk = Frame(root, bg='#FFCC66')
	frame_full_wrk.place(relheight=1, relwidth=1)

	frame_text_wrk = Frame(frame_full_wrk, bg='white',)
	frame_text_wrk.place(relheight=0.07, relwidth=1)

	txt_wrk = Label(frame_full_wrk, text='URL мекенжайыңызды енгізіңіз:', bg='white', font='Impact 50')
	txt_wrk.pack()


	but_wrk = Button(frame_full_wrk, text='Тексеру', bg='red', foreground='white',command=check)
	but_wrk['font']='Impact 17'
	but_wrk.place(relwidth=0.07, relheight=0.06, relx=0.7, rely=0.254)

	frame_text_chk = Frame(frame_full_wrk, bg='white')
	frame_text_chk.place(relx=0.421, rely=0.55, relwidth=0.1, relheight=0.07)


	entry = Entry(frame_full_wrk, font='Arial 35')
	entry.get()
	entry.place(relheight=0.06, relwidth=0.4, relx=0.28, rely=0.254)



	sck = socket.gethostbyname(socket.gethostname())

	sck_txt = Label(frame_full_wrk, text=f"Сіздің IP: {sck}", foreground='red', font='Impact 40', bg='#FFCC66')
	sck_txt.place(relheight=0.06, relwidth=0.4, relx=0.28, rely=0.35)

	del_button = Button(frame_full_wrk, text='Өткен мәнді жою', bg='red', command=delete, foreground='white')
	del_button['font'] = 'Impact 10'
	del_button.place(relheight = 0.05, relwidth=0.07, relx=0.55, rely=0.55)

	extra_text = Label(frame_text_chk, text='Веб-сайттың жауабы', foreground='red', bg='white', font='Impact 12')
	extra_text.pack()


	button_ex = Button(frame_full_wrk, text='X', bg='red', foreground='Black', command=exit)
	button_ex['font'] = 'Impact 30'
	button_ex.place(relx=0.97, rely=0.0001, relheight=0.03, relwidth=0.03)

	but_tutor = Button(frame_full_wrk, text='Мәзірге оралу', bg='red', foreground='white', command=menu)
	but_tutor['font'] = 'Impact 20'
	but_tutor.place(relx=0.43, rely=0.75)





def check():
	global menu, wwb, tutor, wrk, check
	global check_txt
	req = requests.get(entry.get())
	stat = str(req.status_code)


	check_txt = Label(frame_text_chk, text=stat, bg='white', font='Impact 30', foreground='black')
	check_txt.pack()




def delete():
	global menu, wwb, tutor, wrk, check, delete

	check_txt.destroy()




def exit():

	sys.exit()
















menu()
root.mainloop()