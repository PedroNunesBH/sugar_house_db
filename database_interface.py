from tkinter import *
from dotenv import load_dotenv
import mysql.connector
import os

from insert_orders import insert_orders

load_dotenv()

bd_connection = mysql.connector.connect(host=os.getenv("HOST"),
                                        user=os.getenv("USER"),
                                        password=os.getenv("PASSWORD"),
                                        database=os.getenv("DATABASE_NAME"))


cursor = bd_connection.cursor()

main_window = Tk()
main_window.title("Interface Banco de Dados")
main_window.geometry("300x300")
main_window.resizable(width=False, height=False)

label_welcome = Label(main_window, text="Bem Vindo(a)", width=10, font=("Arial", 12, "bold"))
label_welcome.place(x=90, y=20)

insert_order_btn = Button(main_window, text="Inserir Encomenda", command=lambda: insert_orders(cursor, bd_connection), width=16, bg="green", fg="white")
insert_order_btn.place(x=40, y=90)

insert_expense_btn = Button(main_window, text="Inserir Despesa", width=12, bg="green", fg="white")
insert_expense_btn.place(x=170, y=90)

view_information_btn = Button(main_window, text="Visualizar Informações", width=18, bg="green", fg="white")
view_information_btn.place(x=90, y=140)

main_window.mainloop()