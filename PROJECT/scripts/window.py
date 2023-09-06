import tkinter as tk

# Function to handle the button action
def check_password():
    entered_password = password_entry.get()
    
    #TODO: Replace this logic with the actual password 
    correct_password = "mypassword"
    
    if entered_password == correct_password:
        result_label.config(text="Correct password! Access granted.")
    else:
        result_label.config(text="Incorrect password. Try again.")

# Main window configuration
window = tk.Tk()
window.title("Password Game")

# Welcome label
welcome_label = tk.Label(window, text="Welcome to the Password Game!")
welcome_label.pack(pady=10)

# Password entry
password_entry = tk.Entry(window, show="*")  # Password will be displayed as asterisks
password_entry.pack()

# Button to check the password
check_button = tk.Button(window, text="Check Password", command=check_password)
check_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(window, text="")
result_label.pack()

# Start the GUI loop
window.mainloop()
