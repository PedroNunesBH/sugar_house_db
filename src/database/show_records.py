from tkinter import *
from tkinter import messagebox

from database.display_records import display_records

def show_records_window(cursor, bd_connection):
    records_window = Toplevel()
    records_window.title("Escolha uma Tabela")
    records_window.geometry("400x200")
    
    Label(records_window, text="Escolha a tabela que deseja visualizar:", font=("Arial", 12)).pack(pady=10)
    
    Button(records_window, text="Encomendas", command=lambda: display_records("encomendas", cursor, bd_connection)).pack(pady=5)
    Button(records_window, text="Despesas", command=lambda: display_records("despesas", cursor, bd_connection)).pack(pady=5)
