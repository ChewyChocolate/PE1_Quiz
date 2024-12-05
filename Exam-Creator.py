import tkinter as tk
from tkinter import ttk
import sqlite3
import os

def on_add_questions():
    add_qst_window = tk.Toplevel(mainwin)
    add_qst_window.title("Add Question")
    add_qst_window.geometry("400x400")


    lbl_qst_no = ttk.Label(add_qst_window, text="Question No:")
    lbl_qst_no.grid(row=0, column=0, pady=5, padx=5)
    entry_qst_no = ttk.Entry(add_qst_window)
    entry_qst_no.grid(row=0, column=1, pady=5, padx=5)

    lbl_question = ttk.Label(add_qst_window, text="Question:")
    lbl_question.grid(row=1, column=0, pady=5, padx=5)
    entry_question = ttk.Entry(add_qst_window, width=40)
    entry_question.grid(row=1, column=1, pady=5, padx=5)

    lbl_option_a = ttk.Label(add_qst_window, text="Option A:")
    lbl_option_a.grid(row=2, column=0, pady=5, padx=5)
    entry_option_a = ttk.Entry(add_qst_window)
    entry_option_a.grid(row=2, column=1, pady=5, padx=5)

    lbl_option_b = ttk.Label(add_qst_window, text="Option B:")
    lbl_option_b.grid(row=3, column=0, pady=5, padx=5)
    entry_option_b = ttk.Entry(add_qst_window)
    entry_option_b.grid(row=3, column=1, pady=5, padx=5)

    lbl_option_c = ttk.Label(add_qst_window, text="Option C:")
    lbl_option_c.grid(row=4, column=0, pady=5, padx=5)
    entry_option_c = ttk.Entry(add_qst_window)
    entry_option_c.grid(row=4, column=1, pady=5, padx=5)

    lbl_option_d = ttk.Label(add_qst_window, text="Option D:")
    lbl_option_d.grid(row=5, column=0, pady=5, padx=5)
    entry_option_d = ttk.Entry(add_qst_window)
    entry_option_d.grid(row=5, column=1, pady=5, padx=5)

    lbl_answer = ttk.Label(add_qst_window, text="Answer")
    lbl_answer.grid(row=6, column=0, pady=5, padx=5)
    entry_answer = ttk.Entry(add_qst_window)
    entry_answer.grid(row=6, column=1, pady=5, padx=5)


    def save_question():
        qst = entry_qst_no.get()
        question = entry_question.get()
        option_a = entry_option_a.get()
        option_b = entry_option_b.get()
        option_c = entry_option_c.get()
        option_d = entry_option_d.get()
        answer = entry_answer.get()

        if not (qst and question and option_a and option_b and option_c and option_d and answer):
            lbl_status.config(text="All fields are required!", foreground="red")
            return

        if answer.strip() not in {option_a.strip(), option_b.strip(), option_c.strip(), option_d.strip()}:
            lbl_status.config(
                text="Answer must match one of the options (A, B, C, D)!", foreground="red"
            )
            return

        try:
            cursor.execute(
                '''
                INSERT INTO questions (quiz_no, question, optionA, optionB, optionC, optionD, answer)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ''',
                (qst.strip(), question.strip(), option_a.strip(), option_b.strip(), option_c.strip(), option_d.strip(), answer.strip())
            )
            conn.commit()
            lbl_status.config(text="Question added successfully!", foreground="green")
            entry_qst_no.delete(0, tk.END)
            entry_question.delete(0, tk.END)
            entry_option_a.delete(0, tk.END)
            entry_option_b.delete(0, tk.END)
            entry_option_c.delete(0, tk.END)
            entry_option_d.delete(0, tk.END)
            entry_answer.delete(0, tk.END)
        except Exception as e:
            lbl_status.config(text=f"Error: {e}", foreground="red")


    btn_save = ttk.Button(add_qst_window, text="Save Question", command=save_question)
    btn_save.grid(row=7, column=0, columnspan=2, pady=10)

    lbl_status = ttk.Label(add_qst_window, text="")
    lbl_status.grid(row=8, column=0, columnspan=2)

def on_delete_questions():
    delete_qst_window = tk.Toplevel(mainwin)
    delete_qst_window.title("Delete Question")
    delete_qst_window.geometry("400x200")

    lbl_qst_no = ttk.Label(delete_qst_window, text="Question No to Delete:")
    lbl_qst_no.grid(row=0, column=0, pady=5, padx=5)
    entry_qst_no = ttk.Entry(delete_qst_window)
    entry_qst_no.grid(row=0, column=1, pady=5, padx=5)

    lbl_status = ttk.Label(delete_qst_window, text="")
    lbl_status.grid(row=2, column=0, columnspan=2)

    def delete_question():
        qst_no = entry_qst_no.get()
        if not qst_no:
            lbl_status.config(text="Question No is required!", foreground="red")
            return

        try:
            cursor.execute("DELETE FROM questions WHERE quiz_no = ?", (qst_no,))
            conn.commit()
            lbl_status.config(text="Question deleted successfully!", foreground="green")
        except Exception as e:
            lbl_status.config(text=f"Error: {e}", foreground="red")

    btn_delete = ttk.Button(delete_qst_window, text="Delete", command=delete_question)
    btn_delete.grid(row=1, column=0, columnspan=2, pady=10)


def on_edit_questions():
    edit_qst_window = tk.Toplevel(mainwin)
    edit_qst_window.title("Edit Question")
    edit_qst_window.geometry("400x400")

    lbl_qst_no = ttk.Label(edit_qst_window, text="Question No to Edit:")
    lbl_qst_no.grid(row=0, column=0, pady=5, padx=5)
    entry_qst_no = ttk.Entry(edit_qst_window)
    entry_qst_no.grid(row=0, column=1, pady=5, padx=5)

    lbl_question = ttk.Label(edit_qst_window, text="New Question:")
    lbl_question.grid(row=1, column=0, pady=5, padx=5)
    entry_question = ttk.Entry(edit_qst_window, width=40)
    entry_question.grid(row=1, column=1, pady=5, padx=5)

    lbl_option_a = ttk.Label(edit_qst_window, text="New Option A:")
    lbl_option_a.grid(row=2, column=0, pady=5, padx=5)
    entry_option_a = ttk.Entry(edit_qst_window)
    entry_option_a.grid(row=2, column=1, pady=5, padx=5)

    lbl_option_b = ttk.Label(edit_qst_window, text="New Option B:")
    lbl_option_b.grid(row=3, column=0, pady=5, padx=5)
    entry_option_b = ttk.Entry(edit_qst_window)
    entry_option_b.grid(row=3, column=1, pady=5, padx=5)

    lbl_option_c = ttk.Label(edit_qst_window, text="New Option C:")
    lbl_option_c.grid(row=4, column=0, pady=5, padx=5)
    entry_option_c = ttk.Entry(edit_qst_window)
    entry_option_c.grid(row=4, column=1, pady=5, padx=5)

    lbl_option_d = ttk.Label(edit_qst_window, text="New Option D:")
    lbl_option_d.grid(row=5, column=0, pady=5, padx=5)
    entry_option_d = ttk.Entry(edit_qst_window)
    entry_option_d.grid(row=5, column=1, pady=5, padx=5)

    lbl_answer = ttk.Label(edit_qst_window, text="Answer")
    lbl_answer.grid(row=6, column=0, pady=5, padx=5)
    entry_answer = ttk.Entry(edit_qst_window)
    entry_answer.grid(row=6, column=1, pady=5, padx=5)

    lbl_status = ttk.Label(edit_qst_window, text="")
    lbl_status.grid(row=8, column=0, columnspan=2)

    def edit_question():
        qst_no = entry_qst_no.get()
        question = entry_question.get()
        option_a = entry_option_a.get()
        option_b = entry_option_b.get()
        option_c = entry_option_c.get()
        option_d = entry_option_d.get()
        answer = entry_answer.get()

        if not qst_no:
            lbl_status.config(text="Question No is required!", foreground="red")
            return

        try:
            cursor.execute(
                '''
                INSERT INTO questions (quiz_no, question, optionA, optionB, optionC, optionD, answer)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ''',
                (qst_no.strip(), question.strip(), option_a.strip(), option_b.strip(), option_c.strip(), option_d.strip(), answer.strip())
            )
            conn.commit()
            lbl_status.config(text="Question updated successfully!", foreground="green")
        except Exception as e:
            lbl_status.config(text=f"Error: {e}", foreground="red")

    btn_edit = ttk.Button(edit_qst_window, text="Update Question", command=edit_question)
    btn_edit.grid(row=7, column=0, columnspan=2, pady=10)


def on_show_questions():
    show_qst_window = tk.Toplevel(mainwin)
    show_qst_window.title("Show Questions")
    show_qst_window.geometry("600x400")

    try:
        cursor.execute("SELECT * FROM questions")
        questions = cursor.fetchall()

        tree = ttk.Treeview(show_qst_window, columns=("Quiz No", "Question", "Option A", "Option B", "Option C", "Option D", "Answer"), show="headings")
        tree.heading("Quiz No", text="Quiz No")
        tree.heading("Question", text="Question")
        tree.heading("Option A", text="Option A")
        tree.heading("Option B", text="Option B")
        tree.heading("Option C", text="Option C")
        tree.heading("Option D", text="Option D")
        tree.heading("Answer", text="Answer")
        tree.pack(fill=tk.BOTH, expand=True)

        for q in questions:
            tree.insert("", tk.END, values=q)
    except Exception as e:
        lbl_status = ttk.Label(show_qst_window, text=f"Error: {e}")
        lbl_status.pack()


def on_delete_exam():
    delete_exam_window = tk.Toplevel(mainwin)
    delete_exam_window.title("Delete Exam")
    delete_exam_window.geometry("400x200")

    lbl_qst_dlt = ttk.Label(delete_exam_window, text="Are you sure you Want to Delete This Exam?", font=("Arial", 14))
    lbl_qst_dlt.grid(row=0, column=0, columnspan=2, padx=5)

    def on_yes_dlt():
        conn.close()
        os.remove("Exam.db")
        OK_popup = tk.Toplevel(delete_exam_window)
        OK_popup.title("Delete Exam")
        OK_popup.geometry("400x200")
        lbl_exam_deleted = ttk.Label(OK_popup,text="Exam has been Deleted")
        lbl_exam_deleted.pack()

        def on_ok_destroy():
            delete_exam_window.destroy()
            OK_popup.destroy()
        


        btn_OK = ttk.Button(OK_popup, text="OK", command=on_ok_destroy)
        btn_OK.pack()
        
    
    def on_no_dlt():
        delete_exam_window.destroy()


    btn_dlt_yes = ttk.Button(delete_exam_window, text="Yes", command=on_yes_dlt)
    btn_dlt_yes.grid(row=1, column=0, pady=5, padx=5)
    btn_dlt_no = ttk.Button(delete_exam_window, text="No", command=on_no_dlt)
    btn_dlt_no.grid(row=1, column=1, pady=5, padx=5)

def on_exit():
    mainwin.destroy()

# Main Window
mainwin = tk.Tk()
mainwin.geometry("700x700")
mainwin.title("Exam Creator")

conn = sqlite3.connect("Exam.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS questions (
    quiz_no INTEGER,
    question TEXT,
    optionA TEXT,
    optionB TEXT,
    optionC TEXT,
    optionD TEXT,
    answer TEXT
)
''')
conn.commit()

btn_width = 20
btn_height = 2
wgt_padx = 5
wgt_pady = 5

lbltextAbove = ttk.Label(mainwin, text="Welcome to Exam Creator!", font=("Arial", 16))
lbltextAbove.grid(row=0, column=0, columnspan=2, pady=wgt_pady)

btnaddQuestion = ttk.Button(mainwin, text="Add Question", command=on_add_questions, width=btn_width)
btnaddQuestion.grid(row=1, column=0, padx=wgt_padx, pady=wgt_pady)

btndeleteQuestion = ttk.Button(mainwin, text="Delete Question", command=on_delete_questions, width=btn_width)
btndeleteQuestion.grid(row=2, column=0, padx=wgt_padx, pady=wgt_pady)

btneditQuestion = ttk.Button(mainwin, text="Edit Question", command=on_edit_questions, width=btn_width)
btneditQuestion.grid(row=3, column=0, padx=wgt_padx, pady=wgt_pady)

btnshowQuestion = ttk.Button(mainwin, text="Show Question", command=on_show_questions, width=btn_width)
btnshowQuestion.grid(row=4, column=0, padx=wgt_padx, pady=wgt_pady)

btndeleteExam = ttk.Button(mainwin, text="Delete Exam", command=on_delete_exam, width=btn_width)
btndeleteExam.grid(row=5, column=0, padx=wgt_padx, pady=wgt_pady)

btnexit = ttk.Button(mainwin, text="Exit", command=on_exit, width=btn_width)
btnexit.grid(row=6, column=0, padx=wgt_padx, pady=wgt_pady)

mainwin.mainloop()
