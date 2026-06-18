# Image to Pencil Sketch Mini Project
# Required Libraries: OpenCV, NumPy, Tkinter, Pillow

import cv2
import numpy as np
from tkinter import Tk, Button, Label, filedialog
from PIL import Image, ImageTk

# Function to convert image to pencil sketch
def convert_to_sketch():
    file_path = filedialog.askopenfilename(title="Select Image",
                                           filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
    if not file_path:
        return
    
    # Read the image
    image = cv2.imread(file_path)
    
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Invert grayscale
    inverted_image = 255 - gray_image
    
    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    
    # Create pencil sketch using dodge technique
    pencil_sketch = cv2.divide(gray_image, 255 - blurred, scale=256)
    
    # Save the sketch
    save_path = filedialog.asksaveasfilename(defaultextension=".jpg",
                                             filetypes=[("JPEG Image", "*.jpg"),
                                                        ("PNG Image", "*.png")],
                                             title="Save Sketch As")
    if save_path:
        cv2.imwrite(save_path, pencil_sketch)
    
    # Display sketch in GUI
    img = Image.fromarray(pencil_sketch)
    img = ImageTk.PhotoImage(img)
    panel.config(image=img)
    panel.image = img

# GUI Setup
root = Tk()
root.title("Image to Pencil Sketch")
root.geometry("600x600")

btn = Button(root, text="Select Image and Convert to Sketch", command=convert_to_sketch, font=("Arial", 14))
btn.pack(pady=20)

panel = Label(root)
panel.pack(pady=20)

root.mainloop()
import cv2
print(cv2.__version__)

