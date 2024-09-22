from tkinter import *

def insert_orders(cursor, bd_connection):
    def insert_to_bd():
        client_name = entries[0].get()
        quantity = entries[1].get()
        product_name = entries[2].get()
        product_value = entries[3].get()
        promotion = entries[4].get()
        payment_method = entries[5].get()
        delivery_type = entries[6].get()

        insert_query = """INSERT INTO encomendas (s_nomedocliente, i_quantidade, s_nomedoproduto, 
                          f_valordoproduto, s_promocao, s_formadepagamento, s_tipodeentrega)
                          VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        values = (client_name, quantity, product_name, product_value, promotion, payment_method, delivery_type)
        
        try:
            cursor.execute(insert_query, values)
            bd_connection.commit()
            result_label.config(text="Registro inserido com sucesso", fg="green")
            # Limpar os campos após o sucesso
            for entry in entries:
                entry.delete(0, END)
        except Exception as e:
            result_label.config(text=f"Erro ao inserir: {str(e)}", fg="red")

    order_window = Toplevel()
    order_window.title("Inserir Registro de Encomenda")
    order_window.geometry("400x400")
    order_window.resizable(width=False, height=False)

    label_title = Label(order_window, text="Insira um registro", width=20, font=("Arial", 12, "bold"))
    label_title.place(x=90, y=20)

    labels = ["Nome do Cliente:", "Quantidade:", "Nome do Produto:", 
              "Valor do Produto:", "Promoção (Sim/Não):", 
              "Forma de Pagamento:", "Tipo de Entrega:"]

    entries = []
    for i, label_text in enumerate(labels):
        label = Label(order_window, text=label_text)
        label.place(x=20, y=60 + i * 30) 
        entry = Entry(order_window)
        entry.place(x=180, y=60 + i * 30, width=200)
        entries.append(entry)

    button_save = Button(order_window, text="Salvar Encomenda", command=insert_to_bd, bg="green", fg="white")
    button_save.place(x=150, y=300)

    # Label para mostrar o resultado da inserção
    result_label = Label(order_window, text="", font=("Arial", 10))
    result_label.place(x=20, y=350)
