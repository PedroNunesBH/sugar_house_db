from tkinter import *

def insert_expense(cursor, bd_connection):
    def insert_to_bd():
        description = entries[0].get()
        price = entries[1].get()
        payment_method = entries[2].get()

        insert_query = """INSERT INTO despesas (descricao, valor, forma_pagamento)
                          VALUES (%s, %s, %s)"""
        values = (description, price, payment_method)

        try:
            cursor.execute(insert_query, values)
            bd_connection.commit()
            result_label.config(text="Registro de despesa inserido com sucesso", fg="green")
            for entry in entries:
                entry.delete(0, END)
        except Exception as e:
            result_label.config(text=f"Erro ao inserir: {str(e)}", fg="red")

    expense_window = Toplevel()
    expense_window.title("Insira um registro de Despesa")
    expense_window.geometry("450x300")
    expense_window.resizable(width=False, height=False)

    label_title = Label(expense_window, text="Insira um registro", width=30, font=("Arial", 12, "bold"))
    label_title.place(x=50, y=20)

    labels = ["Descrição:", "Valor:", "Forma de Pagamento:"]

    entries = []
    for i, label_text in enumerate(labels):
        label = Label(expense_window, text=label_text)
        label.place(x=20, y=60 + i * 30)
        entry = Entry(expense_window)
        entry.place(x=180, y=60 + i * 30, width=200)
        entries.append(entry)

    button_save = Button(expense_window, text="Salvar Despesa", command=insert_to_bd, bg="green", fg="white")
    button_save.place(x=150, y=200)

    result_label = Label(expense_window, text="", font=("Arial", 10))
    result_label.place(x=20, y=250)
