import sqlite3
import os
conn = sqlite3.connect("quiz.db")
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions(
        quiz_no INTEGER,
        question TEXT,
	    optionA TEXT,
        optionB TEXT,
        optionC TEXT,
	    optionD TEXT
               )
               
               ''')


print("welcome to quiz creator!!!")
print("a. add question")
print("b. delete question")
print("c. edit question")
print("d. take quiz")
print("e. show all questions")
print("f. quit")
choice = input()


if choice == "a" or "A":
    while True:
        questNo = input("Questtion no.: ")
        question = input("enter the question: ")
        optionA = input("Option A: ")
        optionB = input("Option B: ")
        optionC = input("Option C: ")
        optionD = input("Option D: ")
        correctAns = input("Correct answer: ")
        os.system("cls")


        cursor.execute('''
            INSERT INTO questions(quiz_no, question, optionA, optionB, optionC, optionD)
            VALUES(?,?,?,?,?,?)       
                       ''', (questNo, question, optionA, optionB, optionC, optionD, correctAns))
        

        y_or_n = ''
        print("do you want to enter another question? (y/n)")
        if y_or_n == "n" or "N":
            break

elif choice == "b" or "B":
    while True:
        questNo = input("Enter the number you want to delete")
        
        cursor.execute('''
            DELETE FROM questions WHERE questNo = ? ''', (questNo))

        y_or_n = ''
        print("do you want to delete another question? (y/n)")
        if y_or_n == "n" or "N":
            break

elif choice == "c" or "C":
    while True:
        questNo = input("Enter the number you want to edit")
        os.system('cls')

        print("what do you want to edit:")
        print("a. question")
        print("b. option")





        # cursor.execute('''
        #     UPDATE questions WHERE questNo = ? set 
        #                ''')
