from tkinter import *
from cell import Cell
import settings
import utils


root = Tk()
# Override the setting of the window
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='red', # change later
    width=settings.WIDTH,
    height=utils.height_prct(25)
)
top_frame.place(x=0, y=0)

right_frame = Frame(
    root,
    bg='blue', # Change later
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
right_frame.place(x=utils.width_prct(75), y=utils.height_prct(25))

center_frame =Frame(
    root,
    bg='green', # Change later
    width=utils.width_prct(75),
    height=utils.height_prct(75),
)
center_frame.place(
    x=utils.width_prct(0),
    y=utils.height_prct(25),
)

c1 = Cell()
c1.create_btn_object(center_frame)
c1.create_btn_object.place(
    x=0, y=0
)

# Run the window
root.mainloop()
