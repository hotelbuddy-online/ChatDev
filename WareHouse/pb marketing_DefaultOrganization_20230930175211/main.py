import tkinter as tk
from booking import BookingManager
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Palm Beach Bungalows Booking")
        self.geometry("400x300")
        self.booking_manager = BookingManager()
        self.create_widgets()
    def create_widgets(self):
        # Create GUI elements
        self.bungalow_label = tk.Label(self, text="Available Bungalows:")
        self.bungalow_label.pack()
        self.bungalow_listbox = tk.Listbox(self)
        self.bungalow_listbox.pack()
        self.book_button = tk.Button(self, text="Book", command=self.book_bungalow)
        self.book_button.pack()
        self.cancel_button = tk.Button(self, text="Cancel", command=self.cancel_booking)
        self.cancel_button.pack()
        self.refresh_button = tk.Button(self, text="Refresh", command=self.refresh_bungalows)
        self.refresh_button.pack()
        self.status_label = tk.Label(self, text="")
        self.status_label.pack()
        # Load available bungalows
        self.refresh_bungalows()
    def refresh_bungalows(self):
        # Clear the listbox
        self.bungalow_listbox.delete(0, tk.END)
        # Get available bungalows from the booking manager
        available_bungalows = self.booking_manager.get_available_bungalows()
        # Add bungalows to the listbox
        for bungalow in available_bungalows:
            self.bungalow_listbox.insert(tk.END, bungalow)
    def book_bungalow(self):
        # Get selected bungalow from the listbox
        selected_bungalow = self.bungalow_listbox.get(tk.ACTIVE)
        # Make a booking for the selected bungalow
        booking_id = self.booking_manager.make_booking(selected_bungalow, "Guest Name", "Check-in Date", "Check-out Date")
        # Update status label
        self.status_label.config(text=f"Booking ID: {booking_id} - Bungalow {selected_bungalow} booked successfully!")
        # Refresh the list of available bungalows
        self.refresh_bungalows()
    def cancel_booking(self):
        # Get selected booking from the listbox
        selected_booking = self.bungalow_listbox.get(tk.ACTIVE)
        # Cancel the selected booking
        self.booking_manager.cancel_booking(selected_booking)
        # Update status label
        self.status_label.config(text=f"Booking {selected_booking} cancelled successfully!")
        # Refresh the list of available bungalows
        self.refresh_bungalows()
if __name__ == "__main__":
    app = Application()
    app.mainloop()