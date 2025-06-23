import tkinter as tk
# Create a Function to calculate the total amount
def calculate_total():
    try:
        burger = int(entry_burger.get())
        fries = int(entry_fries.get())
        drink = int(entry_drink.get())
        ice_cream = int(entry_ice_cream.get())
        chicken = int(entry_chicken.get())
        total = (burger * 300 + fries * 200 + drink * 80 + ice_cream * 100 + chicken * 2000)
# Display the total
        label_total.config(text=f"Total: GBP(£), {total}")
    except ValueError:
        label_total.config(text="Please enter a valid number.")
# Set up the main window
root = tk.Tk()
root.title("Restaurant Management System")
root.geometry("300x400")
# Create the items and entry fields
def create_item(label, entry_var):
    tk.Label(root, text=label).pack()
    entry = tk.Entry(root)
    entry.pack()
    entry_var.append(entry)
# Create an empty list of entries
entries = []
create_item("Burger (GBP(£) 300)", entries)
create_item("Fries (GBP(£) 200)", entries)
create_item("Drink (GBP(£) 80)", entries)
create_item("Ice Cream (GBP(£) 100)", entries)
create_item("Chicken (GBP(£) 2000)", entries)
entry_burger, entry_fries, entry_drink, entry_ice_cream, entry_chicken = entries
# Buttton to calculate the total
tk.Button(root, text="Calculate Total", command=calculate_total).pack(pady = 10)
# Display label
label_total = tk.Label(root, text="Total: GBP(£) 0")
label_total.pack()
# Run the main application
root.mainloop()