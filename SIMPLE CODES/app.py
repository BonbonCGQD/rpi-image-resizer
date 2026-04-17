import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageOps
import os

class ImageResizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RPi LCD Image Resizer")
        self.root.geometry("500x450")
        
        self.selected_file = None
        self.presets = {
            "320x240 (2.8\"/3.2\")": (320, 240),
            "480x320 (3.5\")": (480, 320),
            "800x480 (5\"/7\")": (800, 480),
            "1024x600 (7\")": (1024, 600)
        }
        
        self.setup_ui()

    def setup_ui(self):
        # File Selection
        tk.Label(self.root, text="Step 1: Select Image", font=("Arial", 10, "bold")).pack(pady=(10, 0))
        self.file_label = tk.Label(self.root, text="No file selected", fg="gray")
        self.file_label.pack(pady=5)
        tk.Button(self.root, text="Browse Image", command=self.browse_image).pack(pady=5)

        # Resolution Selection
        tk.Label(self.root, text="Step 2: Choose Target Resolution", font=("Arial", 10, "bold")).pack(pady=(20, 0))
        self.res_var = tk.StringVar(self.root)
        self.res_var.set(list(self.presets.keys())[1]) # Default to 480x320
        self.res_menu = tk.OptionMenu(self.root, self.res_var, *self.presets.keys())
        self.res_menu.pack(pady=5)

        # Resize Mode Selection
        tk.Label(self.root, text="Step 3: Choose Resizing Mode", font=("Arial", 10, "bold")).pack(pady=(20, 0))
        self.mode_var = tk.StringVar(value="Pad")
        modes = [("Pad (Fit with borders)", "Pad"), ("Crop (Fill screen)", "Crop"), ("Stretch (Full screen)", "Stretch")]
        for text, mode in modes:
            tk.Radiobutton(self.root, text=text, variable=self.mode_var, value=mode).pack(anchor="w", padx=150)

        # Action Button
        tk.Button(self.root, text="Resize and Save", command=self.process_image, bg="green", fg="white", font=("Arial", 12, "bold")).pack(pady=30)

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
        if file_path:
            self.selected_file = file_path
            self.file_label.config(text=os.path.basename(file_path), fg="black")

    def process_image(self):
        if not self.selected_file:
            messagebox.showerror("Error", "Please select an image first!")
            return
        
        target_res = self.presets[self.res_var.get()]
        mode = self.mode_var.get()
        
        try:
            with Image.open(self.selected_file) as img:
                img = img.convert("RGB") # Ensure consistent color space
                
                if mode == "Stretch":
                    resized_img = img.resize(target_res, Image.Resampling.LANCZOS)
                
                elif mode == "Pad":
                    # Maintain aspect ratio and pad with black
                    img.thumbnail(target_res, Image.Resampling.LANCZOS)
                    resized_img = Image.new("RGB", target_res, (0, 0, 0))
                    offset = ((target_res[0] - img.size[0]) // 2, (target_res[1] - img.size[1]) // 2)
                    resized_img.paste(img, offset)
                
                elif mode == "Crop":
                    # Maintain aspect ratio and crop excess
                    resized_img = ImageOps.fit(img, target_res, Image.Resampling.LANCZOS)

                # Save dialog
                save_path = filedialog.asksaveasfilename(defaultextension=".png", 
                                                         filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
                if save_path:
                    resized_img.save(save_path)
                    messagebox.showinfo("Success", f"Image saved successfully to:\n{save_path}")
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageResizerApp(root)
    root.mainloop()
