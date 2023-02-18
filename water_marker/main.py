import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import random
import string

SIZE = 200
SMALLER = int(SIZE / 4)
first_image = None
second_image = None
final_image = None

window = tk.Tk()
window.title("Watermarker")
window.config(padx=50, pady=50)

def uploadFile():
    global first_image
    global second_image
    filename = filedialog.askopenfilename()

    first_image = Image.open(filename)
    first_image = first_image.resize((SIZE, SIZE))
    second_image = first_image
    
    first_image = ImageTk.PhotoImage(first_image)
    first_image_final = first_image
    
    canvas = tk.Canvas(width=SIZE, height=SIZE)
    canvas.create_image(0, 0, anchor='nw', image=first_image_final)
    canvas.grid(column=1, row=2, columnspan=2)

def addWatermark():
    global second_image
    global final_image 

    filename = filedialog.askopenfilename()
    image = Image.open(filename)
    image = image.resize((SMALLER, SMALLER))

    second_image.paste(image, (SIZE-SMALLER - 10, SIZE-SMALLER - 10), image)
    final_image = second_image
    second_image = ImageTk.PhotoImage(second_image)

    canvas2 = tk.Canvas(width=SIZE, height=SIZE)
    canvas2.create_image(0, 0, anchor='nw', image=second_image)
    canvas2.grid(column=1, row=4, columnspan=2)

    tk.Button(text='Download', width=20, command=download).grid(column=1, row=5, columnspan=2)

def download():
    global final_image
    letters = string.ascii_lowercase
    name = ''.join(random.choice(letters) for i in range(8))
    final_image.save(f"{name}.jpg", quality=95)
    tk.messagebox.showinfo(title='Download Status', message='Download complete!')


tk.Label(text="Select Image:").grid(column=1, row=1)
tk.Button(text='Upload', width=20, command=uploadFile).grid(column=2, row=1)

tk.Label(text="Add Watermark:").grid(column=1, row=3)
tk.Button(text='Upload', width=20, command=addWatermark).grid(column=2, row=3)




window.mainloop()