import tkinter as tk
from tkinter import WORD
import requests
import random
import time

wordsToType = None
wordsTyped = None
speedLabel = None
startBtn = None
sentence = ''
starttime = ''
wpm = 0

window = tk.Tk()
window.title("Typertest")
window.config(padx=50, pady=50)
typedWords = tk.StringVar()

def get_words():
    global wordsToType
    global wordsTyped
    global sentence
    global startBtn

    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(word_site)
    words = response.content.decode("utf-8")
    words = words.split('\n')
    random_words = random.sample(words, 100)
    sentence = ''
    for r_words in random_words:
        sentence += r_words+' '
    wordsToType['state'] = tk.NORMAL
    wordsTyped['state'] = tk.NORMAL
    wordsToType.delete(1.0, tk.END)
    wordsTyped.delete(1.0, tk.END)
    wordsToType.insert(tk.END, sentence)
    wordsToType['state'] = tk.DISABLED
    startBtn['state'] = tk.DISABLED
    startCounting()

def startCounting():
    global wordsTyped
    global starttime

    wordsTyped['state'] = tk.NORMAL
    starttime = time.time()

def countWords(event):
    global sentence
    global wordsTyped
    global starttime
    global wpm
    global startBtn

    currenttime = time.time()
    words = wordsTyped.get("1.0",tk.END).strip()

    if words in sentence:
        if (currenttime < starttime + 60):
            timeleft = round(60 - (currenttime - starttime));
            wpm = (len(words) / 5)
            speedLabel['text'] = f"You have {timeleft} seconds left!\nYour words per minute is {wpm}."
        else:
            wordsTyped['state'] = tk.DISABLED
            speedLabel['text'] = f"Time's up!\nYour words per minute is {wpm}."
            startBtn['text'] = 'Try again?'
            startBtn['state'] = tk.NORMAL
    else:
        speedLabel['text'] = "Please check your spelling."


tk.Label(text="Words to type").grid(column=1, row=1)
wordsToType = tk.Text(window, height=15, width=30, padx=10, pady=10, wrap=WORD)
wordsToType.insert(tk.END, 'Begin the test to see the words for you to type.')
wordsToType['state'] = tk.DISABLED
wordsToType.grid(column=1, row=2)

tk.Label(text="Type here").grid(column=2, row=1)
wordsTyped = tk.Text(window, height=15, width=30, padx=10, pady=10, wrap=WORD)
wordsTyped.grid(column=2, row=2)
wordsTyped['state'] = tk.DISABLED
wordsTyped.bind('<KeyPress>', countWords)

speedLabel = tk.Label(text="Start to see your speed")
speedLabel.grid(column=1, row=3, columnspan=2)
startBtn = tk.Button(text='Start', width=20, command=get_words)
startBtn.grid(column=1, row=4, columnspan=2)

window.mainloop()