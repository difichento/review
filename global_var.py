<<<<<<< HEAD
from tkinter import Tk
from tkinter import ttk

alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper = alphabet_lower.upper()
alph_len = len(alphabet_upper)

# инициализация окна
window = Tk()
window.title("МЕГА ШИФРАТОР-2999")
window.geometry('700x700')

# добавление вкладок
tab_control = ttk.Notebook(window)
caes = ttk.Frame(tab_control)
vern = ttk.Frame(tab_control)
vig = ttk.Frame(tab_control)
pict = ttk.Frame(tab_control)
tab_control.add(caes, text='Шифр Цезаря')
tab_control.add(vig, text='Шифр Виженера')
tab_control.add(vern, text='Шифр Вернама')
tab_control.add(pict, text='Шифрование в картинку')
tab_control.pack(expand=1, fill='both')
=======
from string import ascii_lowercase, ascii_uppercase
alphabet_lower = ascii_lowercase
alphabet_upper = ascii_uppercase
>>>>>>> da2fa4dd70c943c684f5e805a708e99e2772c3fb
