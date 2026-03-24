import tkinter as tk
from tkinter import messagebox, filedialog, scrolledtext

from translator import text_to_morse, morse_to_text
from audio import play_morse
from file_handler import read_file, write_file

class MorseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Morse Code Translator")
        self.root.geometry("800x600")

        self.build_ui()

    def build_ui(self):
        tk.Label(self.root, text="Morse Code Translator",
                 font=("Arial", 16, "bold")).pack(pady=10)

        # INPUT
        tk.Label(self.root, text="Input (Text or Morse):").pack()
        self.input_box = scrolledtext.ScrolledText(self.root, height=8)
        self.input_box.pack(fill=tk.BOTH, padx=20, pady=10)

        # BUTTONS
        btn_frame = tk.Frame(self.root)
        btn_frame.pack()

        tk.Button(btn_frame, text="Text → Morse",
                  command=self.convert_to_morse).pack(side=tk.LEFT, padx=5)

        tk.Button(btn_frame, text="Morse → Text",
                  command=self.convert_to_text).pack(side=tk.LEFT, padx=5)

        tk.Button(btn_frame, text="🔊 Play",
                  command=self.play_audio).pack(side=tk.LEFT, padx=5)

        tk.Button(btn_frame, text="🗑 Clear",
                  command=self.clear).pack(side=tk.LEFT, padx=5)

        # OUTPUT
        tk.Label(self.root, text="Output:").pack()
        self.output_box = scrolledtext.ScrolledText(self.root, height=8)
        self.output_box.pack(fill=tk.BOTH, padx=20, pady=10)

        # FILE BUTTONS
        file_frame = tk.Frame(self.root)
        file_frame.pack(pady=5)

        tk.Button(file_frame, text="Load File",
                  command=self.load_file).pack(side=tk.LEFT, padx=5)

        tk.Button(file_frame, text="Save Output",
                  command=self.save_file).pack(side=tk.LEFT, padx=5)

    # FIXED FUNCTIONS #

    def convert_to_morse(self):
        text = self.input_box.get("1.0", tk.END).strip()

        if not text:
            messagebox.showwarning("Warning", "Input is empty")
            return

        result = text_to_morse(text)

        self.output_box.delete("1.0", tk.END)
        self.output_box.insert(tk.END, result)

    def convert_to_text(self):
        code = self.input_box.get("1.0", tk.END).strip()

        if not code:
            messagebox.showwarning("Warning", "Input is empty")
            return

        result = morse_to_text(code)

        self.output_box.delete("1.0", tk.END)
        self.output_box.insert(tk.END, result)

    # MAIN FIX: SMART PLAY
    def play_audio(self):
        input_text = self.input_box.get("1.0", tk.END).strip()
        output_text = self.output_box.get("1.0", tk.END).strip()

        if not input_text and not output_text:
            messagebox.showwarning("Warning", "Nothing to play!")
            return

        def is_morse(text):
            return all(c in ".-/ " for c in text)

        # Priority: input → output
        if input_text:
            if is_morse(input_text):
                code = input_text
            else:
                code = text_to_morse(input_text)
        else:
            if is_morse(output_text):
                code = output_text
            else:
                code = text_to_morse(output_text)

        play_morse(code)

    def clear(self):
        self.input_box.delete("1.0", tk.END)
        self.output_box.delete("1.0", tk.END)

    # FILE #

    def load_file(self):
        path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if path:
            content = read_file(path)
            self.input_box.delete("1.0", tk.END)
            self.input_box.insert(tk.END, content)

    def save_file(self):
        path = filedialog.asksaveasfilename(defaultextension=".txt")
        if path:
            content = self.output_box.get("1.0", tk.END)
            write_file(path, content)
            messagebox.showinfo("Success", "File saved successfully")

def run():
    root = tk.Tk()
    app = MorseApp(root)
    root.mainloop()