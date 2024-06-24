import tkinter as tk

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # Convert height from cm to meters
        bmi = weight / (height ** 2)
        result_label.config(text=f"BMI: {bmi:.2f}", fg="#333333", font=("Arial", 16, "bold"))
        
        if bmi < 18.5:
            category_label.config(text="Category: Underweight", fg="#FF5733", font=("Arial", 14, "bold"))
        elif 18.5 <= bmi < 25:
            category_label.config(text="Category: Normal weight", fg="#4CAF50", font=("Arial", 14, "bold"))
        elif 25 <= bmi < 30:
            category_label.config(text="Category: Overweight", fg="#FFA500", font=("Arial", 14, "bold"))
        else:
            category_label.config(text="Category: Obese", fg="#FF5733", font=("Arial", 14, "bold"))
    except ValueError:
        result_label.config(text="Please enter valid numbers", fg="#FF5733", font=("Arial", 12, "italic"))

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")
root.configure(bg="#F0F0F0")

# Create labels and entries for weight and height
weight_label = tk.Label(root, text="Weight (kg):", bg="#F0F0F0", fg="#333333", font=("Arial", 14))
weight_label.grid(row=0, column=0, padx=10, pady=10)
weight_entry = tk.Entry(root, font=("Arial", 14))
weight_entry.grid(row=0, column=1, padx=10, pady=10)

height_label = tk.Label(root, text="Height (cm):", bg="#F0F0F0", fg="#333333", font=("Arial", 14))
height_label.grid(row=1, column=0, padx=10, pady=10)
height_entry = tk.Entry(root, font=("Arial", 14))
height_entry.grid(row=1, column=1, padx=10, pady=10)

# Create a button to calculate BMI
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi, bg="#4CAF50", fg="white", font=("Arial", 14, "bold"))
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=20)

# Create labels to display the result and category
result_label = tk.Label(root, text="", bg="#F0F0F0", font=("Arial", 16, "bold"))
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

category_label = tk.Label(root, text="", bg="#F0F0F0", font=("Arial", 14, "bold"))
category_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Run the main event loop
root.mainloop()
