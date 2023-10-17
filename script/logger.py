import veh_data
import tkinter as tk
from tkinter import scrolledtext

class PrintWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("600x600")
        self.text_area = scrolledtext.ScrolledText(self)
        self.text_area.pack(fill="both", expand=True)
        self.title("Logger")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.text_area.delete(1.0, tk.END)
        self.destroy()

    def print_text_delete(self, text):
        self.text_area.delete('1.0', tk.END)
        self.text_area.insert(tk.END, text)

        self.text_area.tag_config('here_red', foreground='red')
        self.text_area.see(tk.END)

    def print_text_red(self, text):
        self.text_area.mark_set('xxx', tk.END)
        self.text_area.insert('xxx', text, "here_red")
        self.text_area.tag_config('here_red', foreground='red')
        self.text_area.mark_unset("xxx")


    def print_text_green(self, text):
        self.text_area.mark_set('xxx', tk.END)
        self.text_area.insert('xxx', text, "here_green")
        self.text_area.tag_config('here_green', foreground='green')
        self.text_area.mark_unset("xxx")

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self):
        self.data = veh_data.VehData()
        # 主窗口
        self.print_window = None
    def show_logger(self, root):
        self.print_window = PrintWindow(master=root)



    def set_logger(self, data):
        self.data = data

    def print_logger(self):
        self.print_window.print_text_delete(self.data.strData())
        self.print_window.print_text_green("\n")
        if self.data.feature == 0:
            self.print_window.print_text_red("adaptive air conditionor \n")
            self.print_window.print_text_green("adaptive seat & mirror\n")
            self.print_window.print_text_red("wedge suggestion \n")
            self.print_window.print_text_red("features inquire \n")
            self.print_window.print_text_red("sentry mode suggestion \n")
            self.print_window.print_text_red("vehicle height adjust \n")
            self.print_window.print_text_green("quiet vehicle \n")
            self.print_window.print_text_red("traffic light Red-to-green reminder \n")
            self.print_window.print_text_red("local life suggestion \n")
            self.print_window.print_text_green("Fatigue Relief \n")
            self.print_window.print_text_red("adjust FCW sensitivity suggestion \n")