# Purpose: Customer Dashboard GUI to view and generate tokens.
import tkinter as tk
from tkinter import messagebox
import token_manager

class CustomerView(tk.Frame):
    def __init__(self, parent, user, logout_callback):
        super().__init__(parent)
        self.user = user
        self.logout_callback = logout_callback
        
        # Header with user info
        header = tk.Label(self, text=f"Welcome, {user['username']} (Customer)", 
                          font=("Arial", 14, "bold"), pady=10)
        header.pack()

        # Frame for Token Info
        info_frame = tk.Frame(self, pady=20)
        info_frame.pack()
        
        self.status_label = tk.Label(info_frame, text="Your Token Status: ", font=("Arial", 12))
        self.status_label.pack(pady=5)

        self.serving_label = tk.Label(info_frame, text="Currently Serving: ", 
                                      font=("Arial", 12, "bold"), fg="blue")
        self.serving_label.pack(pady=5)

        # Action Buttons
        btn_frame = tk.Frame(self, pady=20)
        btn_frame.pack()

        self.token_btn = tk.Button(btn_frame, text="Take a Token", 
                                   command=self.take_token, width=20, bg="#e1e1e1")
        self.token_btn.pack(pady=5)

        refresh_btn = tk.Button(btn_frame, text="Refresh Status", 
                                command=self.refresh_data, width=20)
        refresh_btn.pack(pady=5)
        
        logout_btn = tk.Button(self, text="Logout", command=self.logout_callback, fg="red")
        logout_btn.pack(side="bottom", pady=10)
        
        # Load initial data
        self.refresh_data()

    def take_token(self):
        # Double check if already has an active token (though button should be disabled)
        existing = token_manager.get_my_token(self.user['id'])
        if existing:
            messagebox.showwarning("Action Denied", f"You already have an active token: #{existing['token_number']}")
            self.refresh_data() # Ensure UI sync
            return

        new_token_num = token_manager.generate_token(self.user['id'])
        messagebox.showinfo("Success", f"Token #{new_token_num} generated successfully!")
        self.refresh_data()

    def refresh_data(self):
        # 1. Update My Token Status
        my_token = token_manager.get_my_token(self.user['id'])
        if my_token:
            status_text = f"Your Token: #{my_token['token_number']} ({my_token['status']})"
            self.status_label.config(text=status_text, fg="green" if my_token['status'] == 'Serving' else "black")
            # Disable taking another token
            self.token_btn.config(state="disabled", bg="#cccccc")
        else:
            self.status_label.config(text="You have no active token.", fg="gray")
            # Enable taking a token
            self.token_btn.config(state="normal", bg="#e1e1e1")

        # 2. Update Current Serving
        serving = token_manager.get_current_serving()
        if serving:
            self.serving_label.config(text=f"Now Serving: Token #{serving['token_number']}")
        else:
            self.serving_label.config(text="Now Serving: No one (Queue Empty)")
