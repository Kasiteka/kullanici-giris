from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

# Tk sınıfını 'window'a atadık.
window = Tk()

# Pencere Başlığı
window.title("Kullanıcı Giriş Ekranı")

window.geometry("390x220")

# Pencereye ikon ekleme/isterseniz ekleyebilirsiniz
window.iconbitmap("")

# Pencerenin yeniden boyutlandıralamaz/ boyutlandırılsın istiyorsanız true yapınız
window.resizable(width=False, height=False)

# Resim
resim = ImageTk.PhotoImage(Image.open("kullanıcı.PNG"))
lresim = Label(window, image=resim)
lresim.place(x=250, y=10)

# Hata mesajımızı yazdıracağız
L3 = Label(window)
L3.place(x=148, y=200)
