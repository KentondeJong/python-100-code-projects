from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter import colorchooser
from PIL import Image, ImageTk


DARK_BROWN = "#9D615F"
RED = "#C67A6F"
ORANGE = "#E49D82"
TAN = "#F5C5A6"
WHITE = "#FFFFFF"
image = False
labels = 0
img = None
canvas = None

text_labels = []
text_inps = []
x_labels = []
x_inps = []
y_labels = []
y_inps = []
font_labels = []
font_inps = []
color_inps = []
colors = []
add_buttons = []
font_size_labels = []
font_size = []
color_canvas = []
lbs = []

def create_label(index):
    global canvas
    props = {
        "text": text_inps[index].get(),
        "x": x_inps[index].get(),
        "y": y_inps[index].get(),
        "font": font_inps[index].get(),
        "color": colors[index][1],
        "size": int(font_size[index].get()),
    }
    lbs.append(canvas.create_text(props["x"], props["y"], text=props["text"], fill=props["color"], font=(props["font"], props["size"], "normal")))


def choose_color_func():
    global colors
    colors.append(colorchooser.askcolor(title="Choose color"))


def upload_photo():
    global image, img, canvas
    filename = filedialog.askopenfilename(initialdir='/Desktop', title='Select Photo', filetypes=[
        ('JPG files', '*.jpg'), ('PNG files', '*.png')])

    canvas = Canvas(width=400, height=400, highlightthickness=0, highlightbackground=RED, bg=RED)
    img = PhotoImage(file=filename)
    canvas.create_image(200, 200, image=img)
    canvas.grid(column=0, row=2, columnspan=4)


def add_label():
    global labels, text_labels, text_inps, x_labels, x_inps, y_labels, y_inps, font_labels, font_inps, color_inps, add_buttons

    current_row = (labels * 2) + 3
    text_labels.append(Label(text="Text: ", fg=WHITE, background=RED, font=("Lato", 24)))
    text_labels[labels].grid(column=0, row=current_row)
    text_inps.append(Entry(width=21))
    text_inps[labels].grid(column=1, row=current_row)

    x_labels.append(Label(text="X: ", fg=WHITE, background=RED, font=("Lato", 24)))
    x_labels[labels].grid(column=2, row=current_row)
    x_inps.append(Entry(width=10))
    x_inps[labels].grid(column=3, row=current_row)

    y_labels.append(Label(text="Y: ", fg=WHITE, background=RED, font=("Lato", 24)))
    y_labels[labels].grid(column=2, row=current_row + 1)
    y_inps.append(Entry(width=10))
    y_inps[labels].grid(column=3, row=current_row + 1)

    font_labels.append(Label(text="Font: ", fg=WHITE, background=RED, font=("Lato", 24)))
    font_labels[labels].grid(column=0, row=current_row+1)
    font_inps.append(Entry(width=21))
    font_inps[labels].grid(column=1, row=current_row+1)

    font_size_labels.append(Label(text="Font size: ", fg=WHITE, background=RED, font=("Lato", 24)))
    font_size_labels[labels].grid(column=0, row=current_row + 2)
    font_size.append(Entry(width=10))
    font_size[labels].grid(column=1, row=current_row + 2)

    color_inps.append(Button(text="Color", command=choose_color_func, highlightbackground=RED))
    color_inps[labels].grid(column=2, row=current_row + 2)
   
    add_buttons.append(Button(text="Add", command=lambda: create_label(index=labels), highlightbackground=RED))
    add_buttons[labels].grid(column=3, row=current_row + 2)

    if (len(text_inps) - 1) > 0:
        labels += 1


window = Tk()
window.title("Image Watermarker")
window.config(padx=50, pady=50, bg=RED)
title_label = Label(text="Watermarker Maker", fg=WHITE, background=RED, font=("Lato", 50))
title_label.grid(column=0, row=0, columnspan=4)

upload_button = Button(text="Upload an image", highlightthickness=0, command=lambda: upload_photo(), highlightbackground=RED)
upload_button.grid(column=0, row=1, columnspan=2)

add_label_button = Button(text="Add a watermark", highlightthickness=0, command=lambda: add_label(), highlightbackground=RED)
add_label_button.grid(column=2, row=1, columnspan=2)



window.mainloop()