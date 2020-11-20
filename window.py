from tkinter import *
import random
from tkinter import messagebox
import lab_stp_v2 as main

class GUI:
	def __init__(self, master):
		self.master = master
		master.title('')
		self.d_width = root.winfo_screenwidth()
		self.d_height = root.winfo_screenheight()
		self.w_width = 1500#int(self.d_width / 2)
		self.w_height = 850#int(self.d_height / 2)
		self.w_x = int(self.d_width / 2 - self.w_width / 2)
		self.w_y = int(self.d_height / 2 - self.w_height / 2)
		master.geometry(f'{self.w_width}x{self.w_height}+{self.w_x}+{self.w_y}')

		self.font = ('Arial', 14)

		self.canvas = Canvas(master, bg='black', highlightthickness=0)
		self.canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

		self.canvas1 = Canvas(self.canvas, bg='#90918B')
		self.canvas1.place(relx=0, rely=0, relwidth=.3, relheight=1)

		self.canvas2 = Canvas(self.canvas)
		self.canvas2.place(relx=.3, rely=0, relwidth=.4, relheight=1)

		self.canvas3 = Canvas(self.canvas, bg='#90918B')
		self.canvas3.place(relx=.7, rely=0, relwidth=.3, relheight=1)

		self.button1 = Button(self.canvas1, text='Ввести вручную', font=self.font, command=self.com1)
		self.button1.place(relx=.25, rely=.45, relwidth=.5, relheight=.1)

		self.button2 = Button(self.canvas2, text='Случайный список', font=self.font, command=self.com2)
		self.button2.place(relx=.25, rely=.45, relwidth=.5, relheight=.1)

		self.button3 = Button(self.canvas3, text='Считать из файла', font=self.font, command=self.com3)
		self.button3.place(relx=.25, rely=.45, relwidth=.5, relheight=.1)

		master.bind('<Escape>', self.exit_func)

	def exit_func(self, event):
		root.destroy()

	def com1(self):
		self.new_window = Toplevel(root)
		self.canvas11 = Canvas(self.new_window, width=500, height=300, bg='#90918B')
		self.canvas11.pack()
		self.text3 = Text(self.canvas11, font=self.font, wrap=WORD)
		self.text3.place(relx=0.01, rely=0.01, relwidth=.98, relheight=.49)
		self.scr = Scrollbar(self.canvas11, command=self.text3.yview)
		self.text3.configure(yscrollcommand=self.scr.set)
		self.button11 = Button(self.canvas11, text='Посчитать время', font=self.font, command=self.sortirovka)
		self.button11.place(relx=.05, rely=.7, relwidth=.9, relheight=.1)
		self.scr.place(relx=.98, rely=.01, relwidth=.02, relheight=.49)

	def com2(self):
		self.new_window = Toplevel(root)
		self.new_window.geometry('500x300')
		self.canvas22 = Canvas(self.new_window, bg='#90918B')
		self.canvas22.place(relx=0, rely=0, relwidth=1, relheight=1)
		self.random_list_of_nums = []
		self.labell = Label(self.canvas22, font=self.font, text='Размер массива: ', bg='#90918B')
		self.labell.place(relx=.05, rely=.55, relwidth=.45, relheight=.1)
		self.microentry = Entry(self.canvas22, font=self.font)
		self.microentry.place(relx=.5, rely=.55, relwidth=.2, relheight=.1)
		self.microentry.bind('<Return>', self.new_array)
		for i in range(5000):
			self.a = random.randint(-2500, 2500)
			self.random_list_of_nums.append(self.a)
		self.text3 = Text(self.canvas22, font=self.font, wrap=WORD)
		self.text3.place(relx=0.01, rely=0.01, relwidth=.98, relheight=.49)
		self.scr = Scrollbar(self.canvas22, command=self.text3.yview)
		self.text3.configure(yscrollcommand=self.scr.set)
		self.button22 = Button(self.canvas22, text='Посчитать время', font=self.font, command=self.sortirovka)
		self.button22.place(relx=.05, rely=.7, relwidth=.9, relheight=.1)
		self.scr.place(relx=.98, rely=.01, relwidth=.02, relheight=.49)
		self.text3.delete('0.0', END)
		self.text3.insert('0.0', str(self.random_list_of_nums))

	def com3(self):
		self.new_window = Toplevel(root)
		self.canvas33 = Canvas(self.new_window, width=500, height=300, bg='#90918B')
		self.canvas33.pack()
		self.entry3 = Entry(self.canvas33, font=self.font)
		self.entry3.place(relx=.01, rely=.01, relwidth=.49, relheight=.1)
		self.entry3.insert(0, 'message.txt')
		self.entry3.configure(state=DISABLED)
		self.button33 = Button(self.canvas33, text='Считать файл', font=self.font, command=self.open_file)
		self.button33.place(relx=.5, rely=.01, relwidth=.49, relheight=.1)
		self.text3 = Text(self.canvas33, font=self.font, wrap=WORD)
		self.text3.place(relx=0.01, rely=0.12, relwidth=.98, relheight=.49)
		self.scr = Scrollbar(self.canvas33, command=self.text3.yview)
		self.text3.configure(yscrollcommand=self.scr.set)
		self.button33 = Button(self.canvas33, text='Посчитать время', font=self.font, command=self.sortirovka)
		self.button33.place(relx=.05, rely=.7, relwidth=.9, relheight=.1)
		self.scr.place(relx=.98, rely=.12, relwidth=.02, relheight=.49)
		self.on_click_id = self.entry3.bind('<Button-1>', self.on_click)

	def on_click(self, event):
		self.entry3.configure(state=NORMAL)
		self.entry3.delete(0, END)

		self.my_entry.unbind('<Button-1>', self.on_click_id)

	def open_file(self):
		self.f = open(self.entry3.get(), encoding='utf-8')
		self.text3.delete('0.0', END)
		for line in self.f:
			self.text3.insert('0.0', line)

	def sortirovka(self):
		self.new_text = self.text3.get("1.0",END).replace('[', '').replace(']', '').replace('\n', '').split(', ')
		for i in range(0, len(self.new_text)): 
			self.new_text[i] = int(self.new_text[i])
		print(self.new_text)
		main.bubble_sort(self.new_text)
		self.new_text = self.text3.get("1.0",END).replace('[', '').replace(']', '').replace('\n', '').split(', ')
		for i in range(0, len(self.new_text)): 
			self.new_text[i] = int(self.new_text[i])
		main.selection_sort(self.new_text)
		self.new_text = self.text3.get("1.0",END).replace('[', '').replace(']', '').replace('\n', '').split(', ')
		for i in range(0, len(self.new_text)): 
			self.new_text[i] = int(self.new_text[i])
		main.insertion_sort(self.new_text)
		self.new_text = self.text3.get("1.0",END).replace('[', '').replace(']', '').replace('\n', '').split(', ')
		for i in range(0, len(self.new_text)): 
			self.new_text[i] = int(self.new_text[i])
		main.quick_sort(self.new_text)
		self.new_text = self.text3.get("1.0",END).replace('[', '').replace(']', '').replace('\n', '').split(', ')
		for i in range(0, len(self.new_text)): 
			self.new_text[i] = int(self.new_text[i])
		main.heap_sort(self.new_text)

	def new_array(self, event):
		# try:
		# 	self.my_size = int(self.microentry.get())
		# 	self.random_list_of_nums = []
		# 	for i in range(self.my_size):
		# 		self.a = random.randint(int(self.my_size/2)*(-1), int(self.my_size/2))
		# 		self.random_list_of_nums.append(self.a)
		# except:
		# 	messagebox.showerror('Ошибка', 'Введите целое число!')
		if self.microentry.get() != '':
			self.my_size = int(self.microentry.get())
		if self.microentry.get() == '':
			self.my_size = 5000
		self.random_list_of_nums = []
		for i in range(self.my_size):
			self.a = random.randint(int(self.my_size/2)*(-1), int(self.my_size/2))
			self.random_list_of_nums.append(self.a)
		self.text3.delete('0.0', END)
		self.text3.insert('0.0', str(self.random_list_of_nums))

root = Tk()
root.resizable(False, False)
my_gui = GUI(root)
root.mainloop()