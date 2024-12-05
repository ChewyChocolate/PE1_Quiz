import tkinter as tk
from tkinter import ttk
import sqlite3

def load_questions():
    try:
        conn = sqlite3.connect("Exam.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM questions")
        questions = cursor.fetchall()
        conn.close()
        return questions
    except Exception as e:
        print(f"Error loading questions: {e}")
        return []

def start_exam():
    questions = load_questions()
    if not questions:
        lbl_status.config(text="No questions available in the database!", foreground="red")
        return

    exam_window = tk.Toplevel(main_window)
    exam_window.title("Take Exam")
    exam_window.geometry("600x400")

    user_answers = {}
    question_index = [0]  # Mutable to allow updates in nested function

    def show_question():
        nonlocal questions
        qst_no, question, option_a, option_b, option_c, option_d, correct_answer = questions[question_index[0]]

        lbl_question.config(text=f"Q{qst_no}: {question}")
        radio_var.set(None)
        rb_option_a.config(text=f"A: {option_a}", value=option_a)
        rb_option_b.config(text=f"B: {option_b}", value=option_b)
        rb_option_c.config(text=f"C: {option_c}", value=option_c)
        rb_option_d.config(text=f"D: {option_d}", value=option_d)

    def next_question():
        user_answers[questions[question_index[0]][0]] = radio_var.get()  # Store user answer
        question_index[0] += 1
        if question_index[0] < len(questions):
            show_question()
        else:
            finish_exam()

    def finish_exam():
        exam_window.destroy()
        calculate_result(user_answers, questions)

    # UI Elements
    lbl_question = ttk.Label(exam_window, text="", wraplength=550, font=("Arial", 14))
    lbl_question.pack(pady=20)

    radio_var = tk.StringVar()
    rb_option_a = ttk.Radiobutton(exam_window, text="", variable=radio_var)
    rb_option_a.pack(anchor="w", padx=20)
    rb_option_b = ttk.Radiobutton(exam_window, text="", variable=radio_var)
    rb_option_b.pack(anchor="w", padx=20)
    rb_option_c = ttk.Radiobutton(exam_window, text="", variable=radio_var)
    rb_option_c.pack(anchor="w", padx=20)
    rb_option_d = ttk.Radiobutton(exam_window, text="", variable=radio_var)
    rb_option_d.pack(anchor="w", padx=20)

    btn_next = ttk.Button(exam_window, text="Next", command=next_question)
    btn_next.pack(pady=10)

    show_question()

def calculate_result(user_answers, questions):
    correct_count = 0
    for qst_no, _, _, _, _, _, correct_answer in questions:
        if user_answers.get(qst_no) == correct_answer:
            correct_count += 1

    result_window = tk.Toplevel(main_window)
    result_window.title("Exam Result")
    result_window.geometry("400x200")

    total_questions = len(questions)
    lbl_result = ttk.Label(
        result_window,
        text=f"You answered {correct_count} out of {total_questions} questions correctly!",
        font=("Arial", 16)
    )
    lbl_result.pack(pady=20)

    btn_close = ttk.Button(result_window, text="Close", command=result_window.destroy)
    btn_close.pack(pady=10)

# Main Window
main_window = tk.Tk()
main_window.geometry("400x200")
main_window.title("Exam Taker")

lbl_welcome = ttk.Label(main_window, text="Welcome to Exam Taker!", font=("Arial", 16))
lbl_welcome.pack(pady=20)

btn_start_exam = ttk.Button(main_window, text="Start Exam", command=start_exam)
btn_start_exam.pack(pady=10)

lbl_status = ttk.Label(main_window, text="", font=("Arial", 12))
lbl_status.pack()

btn_exit = ttk.Button(main_window, text="Exit", command=main_window.destroy)
btn_exit.pack(pady=10)

main_window.mainloop()
