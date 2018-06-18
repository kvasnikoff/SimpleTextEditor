from tkinter import *
import tkinter.filedialog #позволяет открыать и сохранять файлы
from tkinter import messagebox #используем в "о программе"

class TextEditor:

    # Закрываем программу при вызове функции. Static потому что не работает с объектами класса
    @staticmethod
    def quit_app(event=None):
        root.quit()

    def open_file(self, event=None):

        txt_file = tkinter.filedialog.askopenfilename(parent=root,
                                                      initialdir='/Users/gtnz2047/Desktop') #главное окно программы -- root

        if txt_file:

            self.text_area.delete(1.0, END) #очищение текстового виджета #с первый строчки

            with open(txt_file) as _file: #открываем файл и забираем информацию в текстовый виджет
                self.text_area.insert(1.0, _file.read())

                root.update_idletasks() #обновляем текстовый виджет

    def save_file(self, event=None):

        file = tkinter.filedialog.asksaveasfile(mode='w') #открывает "сохранить как" как диалоговое окно
        if file != None:
            data = self.text_area.get('1.0', END) #записываем данные в переменную

            file.write(data) #вписываем данные и закрываем файл
            file.close()

    def new_file(self, event=None): #для нового файла просто очищаем окно
        self.text_area.delete(1.0, END)

    def font_Hel(self, event=None): #задаем шрифт для текстового виджета
        self.text_area.config(font="Helvetica")



    def font_geo(self, event=None):
        self.text_area.config(font="{Georgia}")

    #открывает message box
    @staticmethod
    def show_about(event=None):
        messagebox.showwarning(
            "О программе",
            "Текстовый редактор. 2018. Сделано студентом КМБО-02-17 Квасниковым Петром"
        )

    def __init__(self, root): #root -- главное окно


        root.title("Текстовый редактор") #имя главного окна

        # Defines the width and height of the window
        root.geometry("600x550")

        frame = Frame(root, width=600, height=550) #рамка для организации виджетов внутри окна

        #создает скролбар
        scrollbar = Scrollbar(frame)

        self.text_area = Text(frame, width=600, height=550,
                        yscrollcommand=scrollbar.set, #yscrollcommand присоединяет скролбар к полю с текстом
                        )

        scrollbar.config(command=self.text_area.yview) #когда мы двигаем скролбар, вызывается yview, двигаюшая текст

        scrollbar.pack(side="right", fill="y") #размещаем скролбар справа, двигается по y


        self.text_area.pack(side="left", fill="both", expand=True) #размещаем текстовый блок слева и заполняем все место
        #добавляем возможность "расширять" текст
        frame.pack()


        the_menu = Menu(root) #создаем обьъект меню


        file_menu = Menu(the_menu, tearoff=0) #создаем выдвигающееся, неудаляемое меню файл
        edit_menu = Menu(the_menu, tearoff=0)
        help_menu = Menu(the_menu, tearoff=0)


        file_menu.add_command(label="Открыть", command=self.open_file, accelerator="command-O")
        file_menu.add_command(label="Сохранить", command=self.save_file, accelerator="command-S")
        file_menu.add_command(label="Очистить", command=self.new_file, accelerator="command-N")

        edit_menu.add_command(label="Helvetica", command=self.font_Hel)
        edit_menu.add_command(label="Georgia", command=self.font_geo)

        help_menu.add_command(label="О программе", command=self.show_about, accelerator="command-A")


        #добавляем разделитель
        file_menu.add_separator()

        file_menu.add_command(label="Закрыть программу", command=self.quit_app)

        # добавляем выдвигающееся меню в меню бар
        the_menu.add_cascade(label="Файл", menu=file_menu)
        the_menu.add_cascade(label="Шрифты", menu=edit_menu)
        the_menu.add_cascade(label="Справка", menu=help_menu)

        root.bind('<Command-o>', self.open_file) #добавляем действия на нажатия кнопок
        root.bind('<Command-s>', self.save_file)
        root.bind('<Command-n>', self.new_file)
        root.bind('<Command-a>', self.show_about)
        root.bind('<Command-q>', self.quit_app)


        # показываем меню бар
        root.config(menu=the_menu)

root = Tk() #главное окно
text_editor = TextEditor(root) #создает текстовый редактор

root.mainloop() #программа работает, пока не закроем ее