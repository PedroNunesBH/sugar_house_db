from tkinter import *
from database.edit_record_window import edit_record_window

def display_records(table_name, cursor, bd_connection):
    display_window = Toplevel()
    display_window.title(f"Registros da Tabela {table_name.capitalize()}")
    display_window.geometry("800x800")

    canvas = Canvas(display_window)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar = Scrollbar(display_window, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    scrollable_frame = Frame(canvas)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    cursor.execute(f"SELECT * FROM {table_name}")
    records = cursor.fetchall()

    if not records:
        Label(scrollable_frame, text="Nenhum registro encontrado.", font=("Arial", 12)).pack(pady=10)
        return
    
    columns = [desc[0] for desc in cursor.description]  
    for col_num, col_name in enumerate(columns):
        Label(scrollable_frame, text=col_name, font=("Arial", 10, "bold")).grid(row=0, column=col_num, padx=10, pady=5)

    for row_num, record in enumerate(records):
        for col_num, value in enumerate(record):
            Label(scrollable_frame, text=str(value)).grid(row=row_num+1, column=col_num, padx=10, pady=5)

        Button(scrollable_frame, text="Editar", command=lambda rec=record: edit_record_window(table_name, rec, cursor, bd_connection)).grid(row=row_num+1, column=len(record), padx=10, pady=5)
        