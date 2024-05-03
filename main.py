from capture_window import capture
from model_training import train_model
from boss_detection import detect
from choose_image import detect_from_image
import tkinter as tk

def run():
    # Start by capturing real-time window to process each image in the loop.
    # capture() - but we are saving this until we have image processing ready with a trained model

    root = tk.Tk()
    root.title("Boss Spawn Detection")
    root.geometry("300x300")
    
    # Button for training the model
    train_button = tk.Button(root, text="Train Model", command=lambda: train_model)
    train_button.pack(pady=25)

    # Button for capturing the window for real-time detection
    capture_button = tk.Button(root, text="Real-time Detection", command=lambda: capture)
    capture_button.pack(pady=25)

    # Button for detection with individual images from files
    detect_button = tk.Button(root, text="Detect with Image", command=detect_from_image)
    detect_button.pack(pady=25)

    root.mainloop()


if __name__ == "__main__":
    run()