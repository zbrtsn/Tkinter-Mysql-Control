import tkinter as tk
from tkinter import ttk
import mysql.connector

# MySQL bağlantısı
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="132Dark132.",  # MySQL şifrenizi buraya girin
    database="mydatabase"
)

def veritabaniVeTabloOlustur():
    cursor = mydb.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
    cursor.execute("USE mydatabase")
    cursor.execute("CREATE TABLE IF NOT EXISTS veriler (id INT AUTO_INCREMENT PRIMARY KEY, metin VARCHAR(255))")
    cursor.close()

def veriEkle():
    cursor = mydb.cursor()
    metin = giris.get()
    sql = "INSERT INTO veriler (metin) VALUES (%s)"
    val = (metin,)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()
    # Metin girişini temizleme
    giris.delete(0, tk.END)

def verileriGoster():
    # Verileri göstermeden önce önceki verileri temizle
    for widget in pencere.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()
    
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM veriler")
    rows = cursor.fetchall()
    for index, row in enumerate(rows, start=1):
        etiket = tk.Label(pencere, text=f"{index}. {row}", font="Tahoma 14", bg="lightgray", padx=10, pady=5)
        etiket.pack(anchor="w")
    cursor.close()

def verileriSifirla():
    cursor = mydb.cursor()
    cursor.execute("TRUNCATE TABLE veriler")
    cursor.execute("ALTER TABLE veriler AUTO_INCREMENT = 1")
    mydb.commit()
    cursor.close()
    # Verileri gösterme alanını temizle
    for widget in pencere.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()
    
    # Metin girişini temizleme
    giris.delete(0, tk.END)

# Veritabanı ve tabloyu oluştur
veritabaniVeTabloOlustur()

pencere = tk.Tk()
pencere.geometry("600x450")
pencere.title("Veritabanına Veri Ekleme Uygulaması")
pencere.configure(bg="lightblue")

etiket = tk.Label(
    pencere,
    text="Metin Girin:",
    font="Tahoma 14",
    bg="lightblue"
)
etiket.pack()

giris = tk.Entry(
    pencere,
    width=50,
    bg="white"
)
giris.pack()

butonEkle = tk.Button(
    pencere,
    text="Veritabanına Ekle",
    command=veriEkle,
    bg="green",
    fg="white",
    relief=tk.FLAT,
    width=20,
    font=("Tahoma", 12, "bold")
)
butonEkle.pack(pady=5)

butonGoster = tk.Button(
    pencere,
    text="Verileri Göster",
    command=verileriGoster,
    bg="blue",
    fg="white",
    relief=tk.FLAT,
    width=20,
    font=("Tahoma", 12, "bold")
)
butonGoster.pack(pady=5)

butonSifirla = tk.Button(
    pencere,
    text="Verileri Sıfırla",
    command=verileriSifirla,
    bg="red",
    fg="white",
    relief=tk.FLAT,
    width=20,
    font=("Tahoma", 12, "bold")
)
butonSifirla.pack(pady=5)

pencere.mainloop()

