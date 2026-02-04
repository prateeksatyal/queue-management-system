# Purpose: Staff Dashboard GUI to manage the queue.
import tkinter as tk
from tkinter import messagebox
import token_manager

class StaffView(tk.Frame):
    def __init__(self, parent, user, logout_callback):
        super().__init__(parent)
        self.user = user
        self.logout_callback = logout_callback

        # Header
        tk.Label(self, text=f"Staff Dashboard - {user['username']}", 
                 font=("Arial", 14, "bold"), pady=10).pack()

        # Main Layout: Left (Controls) | Right (List)
        main_content = tk.Frame(self)
        main_content.pack(fill="both", expand=True, padx=20, pady=10)
        
        left_panel = tk.Frame(main_content)
        left_panel.pack(side="left", fill="y", padx=10)
        
        right_panel = tk.Frame(main_content)
        right_panel.pack(side="right", fill="both", expand=True, padx=10)

        # --- Left Panel: Controls ---
        # --- Left Panel: Controls ---
        self.serving_label = tk.Label(left_panel, text="Serving: None", 
                                      font=("Arial", 16, "bold"), fg="blue", pady=20)
        self.serving_label.pack()

        # Added self. to buttons to access them later
        self.call_next_btn = tk.Button(left_panel, text="Call Next Token", command=self.call_next, 
                                       width=20, height=2, bg="#d1e7dd")
        self.call_next_btn.pack(pady=10)
        
        self.complete_btn = tk.Button(left_panel, text="Complete Current", command=self.complete_current, 
                                      width=20)
        self.complete_btn.pack(pady=5)
        
        tk.Button(left_panel, text="Reset Queue", command=self.reset_queue_action, 
                  width=20, bg="#f8d7da").pack(pady=20)

        # --- Right Panel: Pending List ---
        tk.Label(right_panel, text="Pending Tokens:", font=("Arial", 10, "bold")).pack(anchor="w")
        
        self.token_list = tk.Listbox(right_panel, height=15)
        self.token_list.pack(fill="both", expand=True)
        
        # Refresh Button
        tk.Button(self, text="Refresh List", command=self.refresh_data).pack(pady=5)
        
        # Logout
        tk.Button(self, text="Logout", command=self.logout_callback, fg="red").pack(pady=10)

        # Initial Load
        self.refresh_data()

    def refresh_data(self):
        # 1. Update Listbox
        self.token_list.delete(0, tk.END)
        tokens = token_manager.get_pending_tokens()
        if not tokens:
            self.token_list.insert(tk.END, "No pending tokens.")
            # Disable 'Call Next' if no one is waiting
            self.call_next_btn.config(state="disabled", bg="#f0f0f0")
        else:
            # Enable 'Call Next'
            self.call_next_btn.config(state="normal", bg="#d1e7dd")
            for t in tokens:
                # Display format: "Token #X (User: name)"
                self.token_list.insert(tk.END, f"Token #{t['token_number']} - {t['username']}")

        # 2. Update Current Serving Label
        serving = token_manager.get_current_serving()
        if serving:
            self.serving_label.config(text=f"Serving: #{serving['token_number']}")
            # Enable 'Complete Current'
            self.complete_btn.config(state="normal")
        else:
            self.serving_label.config(text="Serving: None")
            # Disable 'Complete Current' if no one is being served
            self.complete_btn.config(state="disabled")

    def call_next(self):
        token_manager.call_next_token()
        self.refresh_data()

    def complete_current(self):
        serving = token_manager.get_current_serving()
        if not serving:
            messagebox.showinfo("Info", "No token is currently being served.")
            return
        token_manager.complete_current_token()
        self.refresh_data()

    def reset_queue_action(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to RESET the entire queue? This deletes all tokens."):
            token_manager.reset_queue()
            self.refresh_data()
            messagebox.showinfo("Reset", "Queue has been reset.")
