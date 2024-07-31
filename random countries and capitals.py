import tkinter as tk
import random

root = tk.Tk()
root.title("Country and Capital Manager")
root.geometry("400x400")

country_entry = tk.Entry(root)
capital_entry = tk.Entry(root)

country_list_label = tk.Label(root, text="Country List: []")
capital_list_label = tk.Label(root, text="Capital List: []")
random_country_label = tk.Label(root, text="Random Country: ")
random_capital_label = tk.Label(root, text="Random Capital: ")

country_list = []
capital_list = []

def add_country_and_capital():
    country = country_entry.get()
    capital = capital_entry.get()
    
    if country and capital:
        country_list.append(country)
        capital_list.append(capital)
        
        country_list_label.config(text=f"Country List: {country_list}")
        capital_list_label.config(text=f"Capital List: {capital_list}")
        
        country_entry.delete(0, tk.END)
        capital_entry.delete(0, tk.END)

def generate_random_country_and_capital():
    if country_list and capital_list:
        length1 = len(country_list)
        length2 = len(capital_list)
        
        random_country_index = random.randint(0, length1 - 1)
        random_capital_index = random.randint(0, length2 - 1)
        
        random_country = country_list[random_country_index]
        random_capital = capital_list[random_capital_index]
        
        random_country_label.config(text=f"Random Country: {random_country}")
        random_capital_label.config(text=f"Random Capital: {random_capital}")

add_button = tk.Button(root, text="Add Country and Capital", command=add_country_and_capital)
generate_button = tk.Button(root, text="Generate Random Country and Capital", command=generate_random_country_and_capital)

country_entry.place(x=50, y=20)
capital_entry.place(x=200, y=20)
add_button.place(x=120, y=50)
country_list_label.place(x=50, y=100)
capital_list_label.place(x=50, y=150)
generate_button.place(x=90, y=200)
random_country_label.place(x=50, y=250)
random_capital_label.place(x=50, y=300)

root.mainloop()
