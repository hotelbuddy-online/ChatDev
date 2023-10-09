import tkinter as tk
class GUI:
    def __init__(self, booking_manager):
        self.booking_manager = booking_manager
        self.root = tk.Tk()
        self.root.title("Palm Beach Bungalows Booking")
        self.root.geometry("400x300")
        self.create_widgets()
    def create_widgets(self):
        # GUI elements and event handlers
        pass
    def run(self):
        self.root.mainloop()