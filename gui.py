import tkinter as tk
from tkinter import ttk
from generators import *
def main():
    def on_confirm():
        selected_item = dropdown_var.get()
        # Number of numebers generated
        input_value = input_var.get()
        if not input_value.isdigit() or int(input_value) <= 0:
            output_text = "Please enter a valid integer greater than zero."
        else:
            # Drop down menu selection
            if selected_item == "linear congruential generation":
                output = linear_congruential_generator(int(input_value))
            output_text = f"You selected: {selected_item}\nNumber of numbers generating: {input_value}\nNumbers generate: {str(output)}"
        
        
        output_box.config(state=tk.NORMAL)  # Enable editing
        output_box.delete(1.0, tk.END)  # Clear previous text
        output_box.insert(tk.END, output_text)  # Display selection
        output_box.config(state=tk.DISABLED)  # Disable editing

    # Create main window
    root = tk.Tk()
    root.title("Random Number Generator")
    root.geometry("600x400")

    # Dropdown menu
    options = ["linear congruential generation", "Option 2", "Option 3"]
    dropdown_var = tk.StringVar()
    dropdown_var.set(options[0])  # Set default value
    dropdown = ttk.Combobox(root, textvariable=dropdown_var, values=options, width=30, state="readonly")
    dropdown.pack(pady=10)
    
    
    # Input textbox - Number of Numbers
    input_var = tk.StringVar()
    input_entry = ttk.Entry(root,width=10, textvariable=input_var)
    input_entry.pack(pady=5)
    
    # # Input textbox - Lower bound
    # input_var = tk.StringVar()
    # input_entry = ttk.Entry(root,width=10, textvariable=input_var)
    # input_entry.pack(pady=5)
    
    # # Input textbox - Upper bound
    # input_var = tk.StringVar()
    # input_entry = ttk.Entry(root,width=10, textvariable=input_var)
    # input_entry.pack(pady=5)
    
    # Confirmation button
    confirm_button = ttk.Button(root, text="Confirm", command=on_confirm)
    confirm_button.pack(pady=5)

    # Output box
    output_box = tk.Text(root, height=15, width=60, state=tk.DISABLED)
    output_box.pack(pady=10)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()