# Purpose: Main application entry point, Login/Register UI, and View Router.
import tkinter as tk
from tkinter import messagebox
import database
import auth
from customer import CustomerView
from staff import StaffView

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("QueueEase - Queue Management System")
        self.state("zoomed")
        self.resizable(True, True)

        # Initialize Container for frames
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.current_frame = None
        
        # Ensure DB tables exist
        database.create_tables()

        # Start at Login Screen
        self.show_login_screen()

    def clear_frame(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = None

    def show_login_screen(self):
        self.clear_frame()
        self.current_frame = LoginRegisterFrame(self.container, self.login_success)
        self.current_frame.pack(fill="both", expand=True)

    def login_success(self, user):
        """Called when login is successful. user is a dict-like row"""
        self.clear_frame()
        role = user['role']
        if role == 'Customer':
            self.current_frame = CustomerView(self.container, user, self.logout)
        elif role == 'Staff':
            self.current_frame = StaffView(self.container, user, self.logout)
        else:
            messagebox.showerror("Error", "Unknown User Role!")
            self.show_login_screen()
            return

        self.current_frame.pack(fill="both", expand=True)

    def logout(self):
        self.show_login_screen()


class LoginRegisterFrame(tk.Frame):
    def __init__(self, parent, on_login_success):
        super().__init__(parent)
        self.on_login_success = on_login_success
        
        tk.Label(self, text="QueueEase System", font=("Arial", 20, "bold")).pack(pady=30)
        
        # Define StringVars
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.role_var = tk.StringVar(value="Customer")

        # Form
        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Username:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        tk.Entry(form_frame, textvariable=self.username_var).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Password:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        tk.Entry(form_frame, textvariable=self.password_var, show="*").grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Role:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        role_frame = tk.Frame(form_frame)
        role_frame.grid(row=2, column=1, sticky="w")
        tk.Radiobutton(role_frame, text="Customer", variable=self.role_var, value="Customer").pack(side="left")
        tk.Radiobutton(role_frame, text="Staff", variable=self.role_var, value="Staff").pack(side="left")

        # Buttons
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=20)
        
        tk.Button(btn_frame, text="Login", command=self.do_login, width=15, bg="#d1e7dd").pack(side="left", padx=10)
        tk.Button(btn_frame, text="Register", command=self.do_register, width=15).pack(side="left", padx=10)

    def do_login(self):
        u = self.username_var.get()
        p = self.password_var.get()
        if not u or not p:
            messagebox.showerror("Error", "Please fill all fields.")
            return

        user = auth.login_user(u, p)
        if user:
            # Check if role matches
            selected_role = self.role_var.get()
            actual_role = user['role']

            if selected_role != actual_role:
                messagebox.showerror("Error", f"Role mismatch! You are registered as {actual_role} but trying to login as {selected_role}.")
                return

            self.on_login_success(user)
        else:
            messagebox.showerror("Error", "Invalid credentials.")

    def do_register(self):
        u = self.username_var.get()
        p = self.password_var.get()
        r = self.role_var.get()
        if not u or not p:
            messagebox.showerror("Error", "Please fill all fields.")
            return

        success = auth.register_user(u, p, r)
        if success:
            messagebox.showinfo("Success", f"User '{u}' registered as {r}! Please Login.")
        else:
            messagebox.showerror("Error", "Username already exists.")

if __name__ == "__main__":
    app = App()
    app.mainloop()
