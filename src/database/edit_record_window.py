from tkinter import *
from tkinter import messagebox

def edit_record_window(table_name, record, cursor, bd_connection):
    edit_window = Toplevel()
    edit_window.title(f"Editar Registro: ID {record[0]}")
    edit_window.geometry("700x700")

    cursor.execute(f"SHOW COLUMNS FROM {table_name}")
    columns = cursor.fetchall()

    entry_fields = []

    for i, column in enumerate(columns):
        col_name = column[0]

        if i == 0:  # ID field (not editable)
            Label(edit_window, text=f"{col_name} (não editável)").pack(pady=5)
            Label(edit_window, text=record[i]).pack(pady=5)
            continue

        Label(edit_window, text=col_name).pack(pady=5)
        entry_field = Entry(edit_window)
        entry_field.pack(pady=5)
        entry_field.insert(0, record[i])
        entry_fields.append(entry_field)

    def save_changes():
        new_values = [entry.get() for entry in entry_fields]
        set_clause = ", ".join([f"{columns[i][0]} = %s" for i in range(1, len(columns))]) 
        query = f"UPDATE {table_name} SET {set_clause} WHERE {columns[0][0]} = %s"  

        try:
            cursor.execute(query, (*new_values, record[0]))  #
            bd_connection.commit()
            messagebox.showinfo("Sucesso", "Registro atualizado com sucesso!")
            edit_window.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar o registro: {e}")

    def delete_record(cursor, bd_connection):
        confirm = messagebox.askyesno("Confirmar Exclusão", "Tem certeza de que deseja excluir este registro?")
        if confirm:
            delete_query = f"DELETE FROM {table_name} WHERE {columns[0][0]} = %s"  # WHERE ID = ?
            try:
                cursor.execute(delete_query, (record[0],))  # delete the record by ID
                bd_connection.commit()
                messagebox.showinfo("Sucesso", "Registro excluído com sucesso!")
                edit_window.destroy()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao excluir o registro: {e}")

    Button(edit_window, text="Salvar Alterações", command=save_changes, bg="green", fg="white").pack(pady=10)
    Button(edit_window, text="Excluir Registro", command=lambda: delete_record(cursor, bd_connection), bg="red", fg="white").pack(pady=10)
