import tkinter as tk
from tkinter import filedialog
from boss_detection import detect

def detect_from_image():
    # Create a file dialog to select an image
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    
    detect(file_path)