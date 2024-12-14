import tkinter as tk
from tkinter import ttk, messagebox

patients = []
doctors = []
appointments = []
users = []

def format_patient_id(patient_id):
    return f"P{patient_id:03}"

def format_doctor_id(doctor_id):
    return f"D{doctor_id:03}"

def format_appointment_id(appointment_id):
    return f"A{appointment_id:03}"

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    position_top = int(screen_height / 2 - height / 2)
    position_right = int(screen_width / 2 - width / 2)
    
    window.geometry(f'{width}x{height}+{position_right}+{position_top}')

def signup():
    def save_user():
        username = entry_username.get()
        password = entry_password.get()

        if username and password:
            for user in users:
                if user['username'] == username:
                    messagebox.showerror("Error", "Username already exists.")
                    return
            
            users.append({"username": username, "password": password})
            messagebox.showinfo("Success", "Signup successful! You can now log in.")
            signup_window.destroy()
        else:
            messagebox.showerror("Error", "All fields are required.")

    signup_window = tk.Toplevel(login_window)
    signup_window.title("Signup")

    tk.Label(signup_window, text="Username:").grid(row=0, column=0)
    tk.Label(signup_window, text="Password:").grid(row=1, column=0)

    entry_username = tk.Entry(signup_window)
    entry_password = tk.Entry(signup_window, show="*")

    entry_username.grid(row=0, column=1)
    entry_password.grid(row=1, column=1)

    tk.Button(signup_window, text="Signup", command=save_user).grid(row=2, column=0, columnspan=2)

    center_window(signup_window, 300, 150)

def login():
    def validate_login():
        username = entry_username.get()
        password = entry_password.get()

        for user in users:
            if user['username'] == username and user['password'] == password:
                messagebox.showinfo("Success", f"Welcome, {username}!")
                login_window.destroy()
                main_app()
                return
        
        messagebox.showerror("Error", "Invalid username or password.")

    global login_window
    login_window = tk.Tk()
    login_window.title("Login")

    tk.Label(login_window, text="Username:").grid(row=0, column=0)
    tk.Label(login_window, text="Password:").grid(row=1, column=0)

    entry_username = tk.Entry(login_window)
    entry_password = tk.Entry(login_window, show="*")

    entry_username.grid(row=0, column=1)
    entry_password.grid(row=1, column=1)

    tk.Button(login_window, text="Login", command=validate_login).grid(row=2, column=0, columnspan=2)
    tk.Button(login_window, text="Signup", command=signup).grid(row=3, column=0, columnspan=2)

    center_window(login_window, 500, 300)
    login_window.mainloop()

def add_patient():
    def save_patient():
        name = entry_name.get()
        age = entry_age.get()
        gender = entry_gender.get()
        contact = entry_contact.get()

        if name and age and gender and contact:
            patient = {
                "id": len(patients) + 1,
                "name": name,
                "age": int(age),
                "gender": gender,
                "contact": contact
            }
            patients.append(patient)
            messagebox.showinfo("Success", f"Patient added successfully with ID: {format_patient_id(patient['id'])}")
            add_patient_window.destroy()
        else:
            messagebox.showerror("Error", "All fields are required.")

    add_patient_window = tk.Toplevel(root)
    add_patient_window.title("Add Patient")

    tk.Label(add_patient_window, text="Patient's Name:").grid(row=0, column=0)
    tk.Label(add_patient_window, text="Age:").grid(row=1, column=0)
    tk.Label(add_patient_window, text="Gender:").grid(row=2, column=0)
    tk.Label(add_patient_window, text="Contact:").grid(row=3, column=0)

    entry_name = tk.Entry(add_patient_window)
    entry_age = tk.Entry(add_patient_window)
    entry_gender = tk.Entry(add_patient_window)
    entry_contact = tk.Entry(add_patient_window)

    entry_name.grid(row=0, column=1)
    entry_age.grid(row=1, column=1)
    entry_gender.grid(row=2, column=1)
    entry_contact.grid(row=3, column=1)

    tk.Button(add_patient_window, text="Save", command=save_patient).grid(row=4, column=0, columnspan=2)

    center_window(add_patient_window, 500, 300)

def view_patients():
    patients_window = tk.Toplevel(root)
    patients_window.title("View Patients")

    tree = ttk.Treeview(patients_window, columns=("PatientID", "Patient's Name", "Age", "Gender", "Contact"), show="headings")
    tree.heading("PatientID", text="Patient ID")
    tree.heading("Patient's Name", text="Patient's Name")
    tree.heading("Age", text="Age")
    tree.heading("Gender", text="Gender")
    tree.heading("Contact", text="Contact Number")
    tree.pack(fill="both", expand=True)

    for patient in patients:
        tree.insert("", tk.END, values=(format_patient_id(patient["id"]), patient["name"], patient["age"], patient["gender"], patient["contact"]))

    center_window(patients_window, 1200, 300)

def add_doctor():
    def save_doctor():
        name = entry_name.get()
        specialization = entry_specialization.get()

        if name and specialization:
            doctor = {
                "id": len(doctors) + 1,
                "name": name,
                "specialization": specialization
            }
            doctors.append(doctor)
            messagebox.showinfo("Success", f"Doctor added successfully with ID: {format_doctor_id(doctor['id'])}")
            add_doctor_window.destroy()
        else:
            messagebox.showerror("Error", "All fields are required.")

    add_doctor_window = tk.Toplevel(root)
    add_doctor_window.title("Add Doctor")

    tk.Label(add_doctor_window, text="Doctor's Name:").grid(row=0, column=0)
    tk.Label(add_doctor_window, text="Specialization:").grid(row=1, column=0)

    entry_name = tk.Entry(add_doctor_window)
    entry_specialization = tk.Entry(add_doctor_window)

    entry_name.grid(row=0, column=1)
    entry_specialization.grid(row=1, column=1)

    tk.Button(add_doctor_window, text="Save", command=save_doctor).grid(row=2, column=0, columnspan=2)

    center_window(add_doctor_window, 500, 300)

def view_doctors():
    doctors_window = tk.Toplevel(root)
    doctors_window.title("View Doctors")

    tree = ttk.Treeview(doctors_window, columns=("DoctorID", "Doctor's Name", "Specialization"), show="headings")
    tree.heading("DoctorID", text="Doctor ID")
    tree.heading("Doctor's Name", text="Doctor's Name")
    tree.heading("Specialization", text="Specialization")
    tree.pack(fill="both", expand=True)

    for doctor in doctors:
        tree.insert("", tk.END, values=(format_doctor_id(doctor["id"]), doctor["name"], doctor["specialization"]))

    center_window(doctors_window, 1000, 300)

def schedule_appointment():
    def confirm_appointment():
        patient_name = combo_patient.get()
        doctor_name = combo_doctor.get()
        appointment_date = entry_date.get()

        confirm_window = tk.Toplevel(schedule_window)
        confirm_window.title("Confirm Appointment")

        tk.Label(confirm_window, text="Confirm Appointment Details:").grid(row=0, column=0, columnspan=2)
        tk.Label(confirm_window, text="Patient's Name:").grid(row=1, column=0)
        tk.Label(confirm_window, text="Doctor's Name:").grid(row=2, column=0)
        tk.Label(confirm_window, text="Appointment Date:").grid(row=3, column=0)

        tk.Label(confirm_window, text=patient_name).grid(row=1, column=1)
        tk.Label(confirm_window, text=doctor_name).grid(row=2, column=1)
        tk.Label(confirm_window, text=appointment_date).grid(row=3, column=1)

        center_window(confirm_window, 300, 150)

        def save_appointment():
            if patient_name and doctor_name and appointment_date:

                patient_id = next((patient["id"] for patient in patients if patient["name"] == patient_name), None)
                doctor_id = next((doctor["id"] for doctor in doctors if doctor["name"] == doctor_name), None)

                if patient_id and doctor_id:
                    appointment = {
                        "id": len(appointments) + 1,
                        "patient_id": patient_id,
                        "doctor_id": doctor_id,
                        "appointment_date": appointment_date
                    }
                    appointments.append(appointment)
                    messagebox.showinfo("Success", f"Appointment scheduled successfully with ID: {format_appointment_id(appointment['id'])}")
                    schedule_window.destroy()
                else:
                    messagebox.showerror("Error", "Invalid patient or doctor.")
            else:
                messagebox.showerror("Error", "All fields are required.")

        tk.Button(confirm_window, text="Yes, Save Appointment", command=lambda: [confirm_window.destroy(), save_appointment()]).grid(row=4, column=0)
        tk.Button(confirm_window, text="No, Cancel", command=confirm_window.destroy).grid(row=4, column=1)

    schedule_window = tk.Toplevel(root)
    schedule_window.title("Schedule Appointment")

    tk.Label(schedule_window, text="Patient's Name:").grid(row=0, column=0)
    tk.Label(schedule_window, text="Doctor's Name:").grid(row=1, column=0)
    tk.Label(schedule_window, text="Appointment Date (YYYY-MM-DD):").grid(row=2, column=0)

    patients_list = [patient["name"] for patient in patients]
    doctors_list = [doctor["name"] for doctor in doctors]

    combo_patient = ttk.Combobox(schedule_window, values=patients_list)
    combo_doctor = ttk.Combobox(schedule_window, values=doctors_list)
    entry_date = tk.Entry(schedule_window)

    combo_patient.grid(row=0, column=1)
    combo_doctor.grid(row=1, column=1)
    entry_date.grid(row=2, column=1)

    tk.Button(schedule_window, text="Save", command=confirm_appointment).grid(row=3, column=0, columnspan=2)

    center_window(schedule_window, 500, 300)

def view_appointments():
    appointments_window = tk.Toplevel(root)
    appointments_window.title("View Appointments")

    tree = ttk.Treeview(appointments_window, columns=("AppointmentID", "Patient's Name", "Doctor's Name", "Date"), show="headings")
    tree.heading("AppointmentID", text="Appointment ID")
    tree.heading("Patient's Name", text="Patient's Name")
    tree.heading("Doctor's Name", text="Doctor's Name")
    tree.heading("Date", text="Date")
    tree.pack(fill="both", expand=True)

    for appointment in appointments:
        patient_name = next(patient["name"] for patient in patients if patient["id"] == appointment["patient_id"])
        doctor_name = next(doctor["name"] for doctor in doctors if doctor["id"] == appointment["doctor_id"])
        tree.insert("", tk.END, values=(format_appointment_id(appointment["id"]), patient_name, doctor_name, appointment["appointment_date"]))

    center_window(appointments_window, 1000, 300)

def main_app():
    global root
    root = tk.Tk()
    root.title("Hospital Management System")

    welcome_label = tk.Label(root, text="Welcome to HealthSync: Your partner for wellness.", font=("Helvetica", 16))
    welcome_label.pack(pady=10)

    ttk.Button(root, text="Add Patient", command=add_patient).pack(pady=5)
    ttk.Button(root, text="View Patients", command=view_patients).pack(pady=5)
    ttk.Button(root, text="Add Doctor", command=add_doctor).pack(pady=5)
    ttk.Button(root, text="View Doctors", command=view_doctors).pack(pady=5)
    ttk.Button(root, text="Schedule Appointment", command=schedule_appointment).pack(pady=5)
    ttk.Button(root, text="View Appointments", command=view_appointments).pack(pady=5)

    center_window(root, 800, 600)

    root.mainloop()

login()