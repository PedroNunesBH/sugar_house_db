from tkinter import *

def show_financial_info(cursor):
    def fetch_data():
        cursor.execute("SELECT SUM(f_valordoproduto) FROM encomendas")
        total_revenue = cursor.fetchone()[0] or 0

        cursor.execute("""SELECT SUM(f_valordoproduto) 
                          FROM encomendas 
                          WHERE MONTH(d_datadavenda) = MONTH(CURRENT_DATE) 
                          AND YEAR(d_datadavenda) = YEAR(CURRENT_DATE)""")
        total_month_revenue = cursor.fetchone()[0] or 0

        cursor.execute("SELECT SUM(valor) FROM despesas")
        total_expenses = cursor.fetchone()[0] or 0

        cursor.execute("""SELECT SUM(valor) 
                          FROM despesas 
                          WHERE MONTH(data_despesa) = MONTH(CURRENT_DATE) 
                          AND YEAR(data_despesa) = YEAR(CURRENT_DATE)""")
        total_month_expenses = cursor.fetchone()[0] or 0

        total_profit = total_revenue - total_expenses
        total_month_profit = total_month_revenue - total_month_expenses

        total_revenue_label.config(text=f"Total de Faturamento: R${total_revenue:.2f}")
        total_month_revenue_label.config(text=f"Total de Faturamento do Mês Atual: R${total_month_revenue:.2f}")
        total_expenses_label.config(text=f"Total de Despesas: R${total_expenses:.2f}")
        total_month_expenses_label.config(text=f"Total de Despesas do Mês Atual: R${total_month_expenses:.2f}")
        total_profit_label.config(text=f"Lucro Total: R${total_profit:.2f}")
        total_month_profit_label.config(text=f"Lucro do Mês Atual: R${total_month_profit:.2f}")

    info_window = Toplevel()
    info_window.title("Informações Financeiras")
    info_window.geometry("400x400")
    info_window.resizable(width=False, height=False)

    label_title = Label(info_window, text="Informações Financeiras", width=30, font=("Arial", 12, "bold"))
    label_title.place(x=50, y=20)

    label_encomendas = Label(info_window, text="ENCOMENDAS", font=("Arial", 12, "bold"))
    label_encomendas.place(x=20, y=60)
    
    total_revenue_label = Label(info_window, text="", font=("Arial", 10))
    total_revenue_label.place(x=20, y=90)

    total_month_revenue_label = Label(info_window, text="", font=("Arial", 10))
    total_month_revenue_label.place(x=20, y=120)

    label_despesas = Label(info_window, text="DESPESAS", font=("Arial", 12, "bold"))
    label_despesas.place(x=20, y=160)

    total_expenses_label = Label(info_window, text="", font=("Arial", 10))
    total_expenses_label.place(x=20, y=190)

    total_month_expenses_label = Label(info_window, text="", font=("Arial", 10))
    total_month_expenses_label.place(x=20, y=220)

    label_lucro = Label(info_window, text="LUCRO", font=("Arial", 12, "bold"))
    label_lucro.place(x=20, y=260)

    total_profit_label = Label(info_window, text="", font=("Arial", 10))
    total_profit_label.place(x=20, y=290)

    total_month_profit_label = Label(info_window, text="", font=("Arial", 10))
    total_month_profit_label.place(x=20, y=320)

    button_fetch = Button(info_window, text="Carregar Informações", command=fetch_data, bg="blue", fg="white")
    button_fetch.place(x=120, y=370)

    fetch_data()
