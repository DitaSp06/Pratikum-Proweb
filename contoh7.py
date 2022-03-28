from tkinter import *
from  tkinter import  ttk
#importing connection
import  mysql.connector
#establishing connection
conn = mysql.connector.connect(
   user='root', password='', host='localhost', database='pythondata')

def register():
    nama1=nama.get()
    nim1=nim.get()
    prodi1=prodi.get()
    jurusan1=jurusan.get()
    asal1=asal.get()
    jenis_kelamin1=jenis_kelamin.get()

    if nama1=='' or nim1==''or prodi1=='' or jurusan1==''or asal1==''or jenis_kelamin1=='':
        message.set("gagal disimpan")
    else:
       cursor = conn.cursor()
       insert_stmt = (
           "INSERT INTO REG(NAMA, NIM, PRODI, JURUSAN, KOTA, JENIS_KELAMIN)"
           "VALUES (%s, %s, %s, %s, %s, %s)"
       )
       if jenis_kelamin1==1:
        data = (nama1, nim1,prodi1, jurusan1, asal1, "Male")
       else:
        data = (nama1, nim1, prodi1, jurusan1, asal1,"Female")
       try:
           cursor.execute(insert_stmt,data)
           conn.commit()
       except:
           conn.rollback()
       message.set("Berhasil disimpan")

def Registrationform():
    global reg_screen
    reg_screen = Tk()
    reg_screen.title("Dita_Edita")
    reg_screen.geometry("350x400")
    global  message;
    global nama
    global nim
    global prodi
    global jurusan
    global asal
    global jenis_kelamin
    nama = StringVar()
    nim = StringVar()
    prodi=StringVar()
    jurusan=StringVar()
    asal=StringVar()
    jenis_kelamin=IntVar()
    message=StringVar()

    Label(reg_screen,width="300", text="Masukkan data dibawah ini", bg="purple",fg="white").pack()

    Label(reg_screen, text="Nama * ").place(x=20,y=40)

    Entry(reg_screen, textvariable=nama).place(x=90,y=42)

    Label(reg_screen, text="Nim * ").place(x=20,y=80)

    Entry(reg_screen, textvariable=nim).place(x=90,y=82)


    Label(reg_screen, text="Prodi * ").place(x=20, y=120)

    Entry(reg_screen, textvariable=prodi).place(x=90, y=122)

    
    Label(reg_screen, text="Jurusan * ").place(x=20, y=160)

    monthchoosen = ttk.Combobox(reg_screen, width=27, textvariable=jurusan)
    monthchoosen['values'] = (' Matematika dan Teknologi Informasi',
                              ' Teknologi Industri dan Proses',
                              ' Teknik Sipil dan Perencanaan',
                              ' Ilmu Kebumian dan Lingkungan',)
    monthchoosen.current()
    monthchoosen.place(x=90, y=162)

    Label(reg_screen, text="Asal * ").place(x=20, y=200)

    monthchoosen = ttk.Combobox(reg_screen, width=27, textvariable=asal)
    monthchoosen['values'] = (' Balikpapan',
                              ' Samarinda',
                              ' Tenggarong',
                              ' Sangatta',
                              ' Berau',
                              ' Jakarta',
                              ' Jogja',
                              ' Malang',
                              ' Bali',)
    monthchoosen.current()
    monthchoosen.place(x=90,y=202)


    Label(reg_screen, text="Jenis_kelamin * ").place(x=20, y=240)

    Radiobutton(reg_screen,text="Male",variable=jenis_kelamin,value=1).place(x=110,y=242)
    Radiobutton(reg_screen, text="Female", variable=jenis_kelamin, value=2).place(x=180, y=242)


    Label(reg_screen, text="",textvariable=message).place(x=95,y=264)

    Button(reg_screen, text="Register", width=10, height=1, bg="purple",command=register).place(x=130,y=300)
    reg_screen.mainloop()

Registrationform()