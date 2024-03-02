from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

tasks = []


def add_task():
    task_string = task_field.get()
    if len(task_string) == 0:
        messagebox.showinfo('Error', 'Field is Empty.')
    else:
        tasks.append(task_string)
        the_cursor.execute('insert into tasks values (?)', (task_string,))
        list_update()
        task_field.delete(0, 'end')


def list_update():
    task_listbox.delete(0, 'end')
    for task in tasks:
        task_listbox.insert('end', task)


def delete_task():
    try:
        the_value = task_listbox.get(task_listbox.curselection())
        if the_value in tasks:
            tasks.remove(the_value)
            list_update()
            the_cursor.execute('delete from tasks where title = ?', (the_value,))
            the_connection.commit()
    except:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')


def delete_all_tasks():
    if messagebox.askyesno('Delete All', 'Are you sure?'):
        tasks.clear()
        the_cursor.execute('delete from tasks')
        list_update()
        the_connection.commit()


def close():
    the_connection.close()
    guiWindow.destroy()


def retrieve_database():
    tasks.clear()
    for row in the_cursor.execute('select title from tasks'):
        tasks.append(row[0])
    list_update()


if __name__ == "__main__":
    guiWindow = Tk()
    guiWindow.title("To-Do List ")
    guiWindow.geometry("400x400")
    guiWindow.resizable(0, 0)

    the_connection = sql.connect('listOfTasks.db')
    the_cursor = the_connection.cursor()
    the_cursor.execute('create table if not exists tasks (title text)')

    task_field = Entry(guiWindow)
    task_field.pack(pady=10)

    add_button = Button(guiWindow, text="Add", command=add_task)
    add_button.pack(pady=5)

    task_listbox = Listbox(guiWindow)
    task_listbox.pack(pady=10)

    delete_button = Button(guiWindow, text="Delete", command=delete_task)
    delete_button.pack(pady=5)

    delete_all_button = Button(guiWindow, text="Delete All", command=delete_all_tasks)
    delete_all_button.pack(pady=5)

    close_button = Button(guiWindow, text="Close", command=close)
    close_button.pack(pady=5)

    retrieve_database()
    guiWindow.mainloop()
