import tkinter as tk
from tkinter import ttk, messagebox
import random  # Placeholder for prediction logic
import pandas as pd  # For exporting summary report


# Function to predict yield
def predict_yield():
    # Placeholder logic for yield prediction
    # This is where you would integrate your ML model
    try:
        crop_type = crop_type_var.get()
        pH_level = float(pH_entry.get())
        n_level = float(n_entry.get())
        p_level = float(p_entry.get())
        k_level = float(k_entry.get())
        moisture = float(moisture_entry.get())

        # Simple prediction logic (this should be replaced with your ML model)
        predicted_yield = random.uniform(2.0, 10.0)  # Simulating yield prediction
        confidence_level = random.uniform(70, 95)  # Simulating confidence

        # Prepare the summary report
        summary = {
            "Crop Type": crop_type,
            "pH Level": pH_level,
            "N Level": n_level,
            "P Level": p_level,
            "K Level": k_level,
            "Moisture Content": moisture,
            "Predicted Yield (tons/hectare)": predicted_yield,
            "Confidence Level (%)": confidence_level
        }

        # Show prediction results
        result_text = f"Predicted Yield: {predicted_yield:.2f} tons/hectare\n"
        result_text += f"Confidence Level: {confidence_level:.2f}%"
        messagebox.showinfo("Prediction Result", result_text)

        # Export to CSV
        df = pd.DataFrame([summary])
        df.to_csv('yield_prediction_summary.csv', index=False)
        messagebox.showinfo("Export", "Summary report exported as yield_prediction_summary.csv")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for soil parameters.")


# Creating the GUI
app = tk.Tk()
app.title("Crop Yield Prediction")

# Crop Type
crop_type_var = tk.StringVar()
crop_label = ttk.Label(app, text="Select Crop Type:")
crop_label.grid(column=0, row=0, padx=10, pady=10)
crop_combo = ttk.Combobox(app, textvariable=crop_type_var)
crop_combo['values'] = ("Wheat", "Corn", "Rice")
crop_combo.grid(column=1, row=0, padx=10, pady=10)

# Soil Parameters
ttk.Label(app, text="pH Level:").grid(column=0, row=1, padx=10, pady=10)
pH_entry = ttk.Entry(app)
pH_entry.grid(column=1, row=1, padx=10, pady=10)

ttk.Label(app, text="N Level (N):").grid(column=0, row=2, padx=10, pady=10)
n_entry = ttk.Entry(app)
n_entry.grid(column=1, row=2, padx=10, pady=10)

ttk.Label(app, text="P Level (P):").grid(column=0, row=3, padx=10, pady=10)
p_entry = ttk.Entry(app)
p_entry.grid(column=1, row=3, padx=10, pady=10)

ttk.Label(app, text="K Level (K):").grid(column=0, row=4, padx=10, pady=10)
k_entry = ttk.Entry(app)
k_entry.grid(column=1, row=4, padx=10, pady=10)

ttk.Label(app, text="Moisture Content:").grid(column=0, row=5, padx=10, pady=10)
moisture_entry = ttk.Entry(app)
moisture_entry.grid(column=1, row=5, padx=10, pady=10)

# Prediction Button
predict_button = ttk.Button(app, text="Predict Yield", command=predict_yield)
predict_button.grid(column=0, row=6, columnspan=2, padx=10, pady=20)

# Start the GUI loop
app.mainloop()