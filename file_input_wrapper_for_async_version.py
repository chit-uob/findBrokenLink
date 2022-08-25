import find_broken_link_with_async
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

find_broken_link_with_async.path = file_path

find_broken_link_with_async.main()

input("Press enter to exit ;)")