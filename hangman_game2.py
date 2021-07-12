import tkinter as tk
import random
import json
from tkinter import messagebox

f = open("dictionary.json")
data = json.load(f)

global random_word
global word_meaning
global button_2
global iii
iii = 4


def fill(random_word, user_word, output_word):
    output_word = output_word.split()
    user_word = list(user_word)  # changing a string into a list
    random_word = list(random_word)
    if(len(user_word) >= len(random_word)):
        for i in range(len(random_word)):
            if(user_word[i] == random_word[i]):
                output_word[i] = random_word[i]
    else:
        for i in range(len(user_word)):
            if(user_word[i] == random_word[i]):
                output_word[i] = random_word[i]
    output_word = " ".join(output_word)  # changning of list into a string
    return output_word


def makethis():
    global my_label1, my_label2, my_label3, output_word
    global random_word
    output_word = list(random_word)
    for i in range(len(random_word)):
        if((i != 0) and (i != (len(random_word) - 1))):
            output_word[i] = " _ "

    output_word = "".join(output_word)

    my_label3.config(text=output_word)

def trythis():

    global random_word
    global word_meaning
    global iii
    global button_2

    iii = 4
    random_word, word_meaning = random.choice(list(data.items()))
    # e.delete(0, tk.END)
    # e.insert(0, random_word)
    button_2 = tk.Button(root, text="try again", padx=30, pady=10, command=trythis).grid(
        row=6, column=1, ipady=10)

    my_label.config(
        text=f'congrats the game is started you have {iii} chances')
    makethis()


# def dothing1():
#     global iii
#     dothing(iii)


def dothing(i):
    global output_word, random_word, my_label3
    x = e1.get()
    e1.delete(0, tk.END)
    if x == random_word:
        my_label.config(text=f'congrats you completed the game')
        res = messagebox.askyesno(
            "thanks for participation", f'        you won the game\n do you want to try again?')
        if(res):
            trythis()
        else:
            root.destroy()

    else:
        global iii
        if(iii != 0):
            e1.delete(0, tk.END)
            my_label.config(
                text=f'np try again, you have still {iii} chances more')
            output_word = fill(random_word, x, output_word)
            my_label3.config(text=output_word)
            iii = iii - 1
        else:
            res = messagebox.askyesno(
                "thanks for participation", f'        you last the game\n do you want to try again?')
            if(res):
                trythis()
            else:
                root.destroy()


root = tk.Tk()
root.title("hangman game")

# global e
# e = tk.Entry(root, font=10, width=30, borderwidth=5)
# e.grid(row=4, column=0, columnspan=5, padx=10, pady=10, ipady=12)

global e1
e1 = tk.Entry(root, font=10, width=30, borderwidth=5)
e1.grid(row=5, column=0, columnspan=5, padx=10, pady=10, ipady=12)


def check(event):
    e1.insert(len(e1.get()), event.keysym)


global my_label
my_label = tk.Label(
    root, text="U can do it,press start to start game", font=(12))
my_label.grid(column=0, row=0, columnspan=6)

button_1 = tk.Button(root, text="check", padx=30, pady=10, command=lambda: dothing(iii)).grid(
    row=6, column=0, ipady=10)
button_2 = tk.Button(root, text="start", padx=30, pady=10, command=trythis).grid(
    row=6, column=1, ipady=10)
my_label1 = tk.Label(root, text="       ", font=(12))
my_label.grid(column=0, row=1, columnspan=5)

my_label2 = tk.Label(root, text="         ", font=(12))
my_label.grid(column=0, row=2, columnspan=5)

my_label3 = tk.Label(root, text="", font=(12))
my_label3.grid(column=0, row=3, columnspan=5)
# root.bind("<Enter>", lambda x: dothing1())

root.mainloop()
