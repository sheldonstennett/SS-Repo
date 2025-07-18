# Program: Hospital Management System (HMS)

#Module
import random


def is_time_available(schedule,time,date):
    return (date, time) not in schedule

def generated_id(prefix):
    return prefix + str(random.randint(10000,99999))


# PERSON CLASS (PARENT CLASS/SUPER CLASS)
# Attributes of Person Class (name, age gender)
class Person:
    def __init__(self, name, age, gender):      #   Constructor Method
        self.name = name                        #Attribute
        self.age = age                          #Attribute
        self.gender = gender                    #Attribute
    def display_info(self):                     # Display Patient Information Method
        print(f"Patient Info: {self.name}, Age: {self.age}, Gender: {self.gender}")


# PATIENT CLASS (CHILD CLASS/ SUB CLASS OF PERSON)
# Inherits attributes (name, age, gender) from person class.

class Patient(Person):
    def __init__(self, name, age, gender):       # Constructor Method
        super().__init__(name, age, gender)      # Attributes from Person class
        self.patient_id = generated_id("PAT-")   #Attribute
        self.appointment_list = []               #Attribute


    # BOOKING APPOINTMENT AND VIEWING PATIENT E-DOCKETS/ PROFILE

    def add_appointment(self, appointment):             # Add/ book appointment method
        self.appointment_list.append(appointment)       #Attribute

    def view_profile(self):                             # View Patient Profile Method
        print("\n Patient Docket Info")
        self.display_info()                             # Display Patient name, age, gender
        print(f"Patient ID: {self.patient_id}")
        print("Appointments: ")
        if self.appointment_list:                       # Has appointments stored. doctor name, appointment date and appointment time.
            for app in self.appointment_list:
                print(f"Appoint to Dr. {app.doctor.name} on {app.date} at {app.time}")
        else:
            print("There is currently no appointment scheduled. Kindly set one at your earliest convenience.")


# DOCTOR CLASS (CHILD CLASS/ SUB CLASS OF PERSON CLASS)
#  Inherits attributes (name, age, gender) from person class.

class Doctor(Person):
    def __init__(self, name, age, gender, speciality):      # Constructor Method
        super().__init__(name, age, gender)                 # Attributes from Person class

        self.doctor_id = generated_id("DOC-")                  # Attribute
        self.speciality = speciality                           # Attribute
        print(f"Doctor Details: Age- {self.age}, Gender- {self.gender}")
        print(f"Speciality: {self.speciality}")
        self.schedule = []            # Attribute (Stores schedule for doctor in list)


    def is_available (self, date, time):                        # Method
        return is_time_available(self.schedule, date, time)

    def view_schedule(self):                                    # Method
        print(f"Appointment scheduled for Dr. {self.name}")
        if self.schedule:
               for date,time in self.schedule:
                   print(f"{date} at {time}")
        else:
            print("No appointment scheduled.")


#APPOINTMENT CLASS / SCHEDULING
class Appointment:
    def __init__(self, patient, doctor, date,time):   #Construct method
        self.appointment_id = generated_id("APP-")
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time
        self.status = f"Your appointment number is {self.appointment_id}. It has been successfully scheduled for {self.date} at {self.time}."

    def confirm (self):          # Confirmation Method (Printing confirmation with appointment id , time and date)
        print(f"\nYour appointment {self.appointment_id} has been successfully scheduled for {self.date} at {self.time}.")

    def cancel (self):           # Cancel Method
        print(f"I regret to inform you that your appointment {self.appointment_id} for {self.date} at {self.time} has been cancelled.")

# HOSPITAL SYSTEM CLASS
class HospitalSystem:
    def __init__(self):
        self.patient = {}               # Dictionary that stores patient info
        self.doctor = {}                # Dictionary that stores doctor info
        self.appointment = {}           # Dictionary that stores appointment info

    def add_patient(self, name, age, gender):       # Method (Adding new patients)
        try:
            age = int(age)                   # Error validation if age is not an integer
        except ValueError:
            print("Please enter a valid age.")

        if age <= 0:                         # Error validation if age is lesser or equal to zero. Must be greater than 0
            print("Age Invalid!")

        if gender.lower() not in ["male", "female"]:   # Error validation if gender is not male of female
            print("Gender Invalid!")
            return
        patient = Patient(name, age, gender)           # Object of the Patient class.
        self.patient[patient.patient_id] = patient      # Stores patient info in the patient dictionary and generate ID
        print(f"\nRegistration Done")
        print(f"Patient ID number is: {patient.patient_id}\n")


    def add_doctor(self, name, age, gender, speciality):    # Method ( Adding new doctors and generating ID for doctors)
        doctor = Doctor(name, age, gender, speciality)      # Object ( of the doctor class)
        self.doctor[doctor.doctor_id] = doctor              # Calling doctor ID from the doctor class
        print(f"\n Doctor information saved successfully. Doctor ID number is:{doctor.doctor_id}")

    def book_appointment(self, patient_id, doctor_id, date, time):  # Method ( Adding or booking appointments)
        patient = self.patient.get(patient_id)                      # Getting Patient ID from Patient Class
        doctor = self.doctor.get(doctor_id)                         # Getting Doctor ID from Doctor Class

        if not patient:                     # Error validation if patient ID does not match patient in register
            print(f"No patient located with ID: {patient_id}")
        elif not doctor:                     # Error validation if doctor ID does not match doctor in register
            print(f"No doctor located with ID: {doctor_id}")
            return
        if not doctor.is_available(date,time):
            print("Doctor is booked")
            return

        appointment = Appointment(patient,doctor,date,time)         # Object of the appointment class.
        self.appointment[appointment.appointment_id] = appointment  # Stores appointment in the appointment dictionary
        patient.add_appointment(appointment)            # Calling the add appointment method from the patient class
        doctor.schedule.append((date,time))             # To update the doctor schedule dictionary in doctor class
        appointment.confirm()                           # getting the confirm method from the appointment class


    def cancel_appointment(self, appointment_id):         # Method (Displays cancelled appointment with ID number)
        appointment = self.appointment.get(appointment_id)  # Object ( gets appointment ID from the appointment class)
        if appointment:
            appointment.cancel()                    # Getting the cancel method from the appointment class
            print(f"Appointment {appointment_id} cancelled.")

        else:                                     # If appointment ID entered not found then this displays ID not found
            print(f"The scheduled appointment {appointment_id} not found")

    def generate_bill(self, appointment_id):        # Method (Generates total_bill for patient)
        appointment = self.appointment.get(appointment_id)  # get appointment from appointment dictionary
        if not appointment:
            print(f"No appointment found with ID: {appointment_id}")
            return

        # Bill details

        hospital_name = "SS HOSPITAL"                           # Hospital name
        address = "876 Indigo Lane, Rosewood Hills, Hanover"    # Hospital address
        tel = "876-956-8455"                                    # Hospital Telephone
        email = "sshospital876@gmail.com"                       # Hospital email
        print("\n=====================================================================================")
        print(f"\n-----------------{hospital_name}-----------------")
        print(f"\n      Address: {address}")
        print(f"        Tel: {tel}")
        print(f"         Email: {email}")
        print(f"\nPatient name: {appointment.patient.name}")
        print(f"Doctor visited: {appointment.doctor.name}")
        print(f"Date and Time of visit: {appointment.date} at {appointment.time}")
        print("\n=======================================================================================")

        consultation_fee = 3000                         #   Consultation fee
        print(f"\nConsultation is ${consultation_fee} JMD")
        try:
            additional_service_fees = float(input("\nEnter applicable service fees for prescribed medications and diagnostic tests: JMD $"))
        except ValueError:
            print("Please enter additional service fees!")
            additional_service_fees = 0 or ()

        total_bill = consultation_fee + additional_service_fees        # Total bill calculation for patient
        print(f"Your total payment comes to $ {total_bill} JMD \n ")
        print(f"Thanks for choosing {hospital_name}")
        print("======================================================================================")


def main_menu():                     # Method (generates menu for the user to select from)
    hospital = HospitalSystem()    # Object of the Hospital system class
    app = Appointment               # Object of the appointment class

    while True:
        hospital_name = "SS HOSPITAL"
        print()
        print("\n*************************************************************************************")
        print(f"                       {hospital_name} Management System")
        print("-------------------------------------------------------------------------------------")
        print("Select your preferred selection from the following menu below:")
        print()
        print("NP - Register New Patient")
        print("ND - Record New Doctor")
        print("BA - Book Appointment")
        print("CA - Cancel Appointment")
        print("PP - View Patient Details/ Profile")
        print("DP - View Doctor Profile")
        print("GB - Generate Patient Bill")
        print("EX - Exit")
        print("**************************************************************************************\n")

        """
        Below are the actions for selected options by user.

             """

        while True:
            selection = input("\n Please make your selection from the menu above: ").strip().upper()
            if selection == "":                                        # Error validation if nothing is selected
                print("Nothing selected. Please enter a selection.")
            elif not selection.replace("","").isalpha(): # Error validation if numbers where selected
                print("Unfortunately selection should be letters. Please enter the two letter that corresponds with selection.")
            else:
                 break


        if selection == "NP":

            while True:
                name1 = input("\nPatient First Name: ").strip().title()    # capitalizeS the fist words in a string
                if name1 == "":                                          # Error validation if nothing is selected
                    print("First name is empty. Please enter a first name.")
                elif not name1.replace("","").isalpha():    # Error validation if numbers where selected
                    print("First name should be letters. Please enter a first name.")
                else:
                    break

            while True:
                name2 = input("Patient Last Name: ").strip().title()
                if name2 == "":                                                  # Error validation if nothing is selected
                    print("Last name is empty. Please enter a last name.")
                elif not name2.replace("", "").isalpha():         # Error validation if numbers where selected
                    print("Last name should be letters. Please enter a last name.")
                else:
                    break

            name = f"{name1} {name2}"

            while True:
                try:
                    age = int(input("Age: ").strip())
                    if age >= 1:                            # Error Validation if a number less than 1 was selected
                        break
                    else:
                        print("Age must be greater than 0. Please try again.")
                except ValueError:                          # Error Validation is any other than an integer was selected
                    print("Invalid age. Please enter a number for age.")

            while True:
                gender = input("Gender: ").lower().strip()
                if gender in ["male","female"]:                # Error validation if any other entry than male or female is selected

                    break
                else:
                    print("Invalid gender, entry should be male or female.")

            hospital.add_patient(name, age, gender)       # Calling the add patient method from hospital system class

        elif selection == "ND":

            while True:
                name1 = input("\nDoctor First Name: ").strip().title()   # capitalize the fist words in a string
                if name1 == "":                                            # Error validation if nothing is selected
                    print("First name is empty. Please enter a first name.")
                elif not name1.replace("", "").isalpha():
                    print("Doctor first name should be letters. Please enter a first name.")
                else:
                    break

            while True:
                name2 = input("Doctor Last Name: ").strip().title()
                if name2 == "":                                           # Error validation if nothing is selected
                    print("Last name is empty. Please enter a last name.")
                elif not name2.replace("", "").isalpha():
                    print("Last name should be letters. Please enter a last name.")
                else:
                    break

            name = f"{name1} {name2}"

            while True:
                speciality = input("Doctor Speciality: ").strip().title()
                if speciality == "":                                    # Error validation if nothing is selected
                    print("No speciality entered. Please enter speciality!" )
                elif not speciality.replace("","").isalpha():
                    print("Speciality should be letters. Please enter speciality")
                else:
                    break

            while True:
                try:
                    age = int(input("Age: ").strip())
                    if age >= 1:                            # Error Validation if age is less than 1
                        break
                    else:
                        print("Age must be greater than 0. Please try again.")

                except ValueError:                          # Error Validation if any other entry than age is entered
                    print("Invalid age. Please enter a number for age.")

            while True:
                gender = input("Gender: ").lower().strip()
                if gender in ["male","female"]:             # Error validation if any other entry than male or female is selected

                    break
                else:
                    print("Invalid doctor gender, please input male or female.")

            hospital.add_doctor(name, age, gender,speciality)           # Calling the add doctor method from hospital system class

        elif selection == "BA":
            while True:
                patient_id = input("Enter Patient ID: ").strip().upper()
                if patient_id:                                              # Error validation if nothing is selected
                    break
                else:
                    print("Patient ID is empty. Please enter ID.")

            while True:
                doctor_id = input("Enter Doctor ID: ").strip().upper()
                if doctor_id:                                               # Error validation if nothing is selected
                    break
                else:
                    print("Doctor ID is empty. Please enter ID.")

            from datetime import datetime                        # Accesses the datetime class from the date time module

            while True:
                date_entered = input("Enter appointment date (DD-MM-YYYY): ").strip()
                try:
                    date = datetime.strptime(date_entered, "%d-%m-%Y")     # Converts date entered into the date and time format
                    date_only = date.date()                                     # Takes only the date from the datetime class ( displays date only)
                    break
                except ValueError:
                    print("Invalid date. Please use DD-MM-YYYY.")

            while True:
                time_entered = input("Enter appointment time (HH:MM am/pm): ").strip()
                try:
                    time_only = datetime.strptime(time_entered, "%I:%M %p")  # Converts time entered into the time format
                    only_time = time_only.time()                        # Takes only the time from the datetime class ( displays time only)
                    twelve_hr_time = only_time.strftime("%I:%M %p")     # Converts time entered into 12-hour time format
                    break
                except ValueError:
                    print("Invalid time. Please use HH:MM am/pm.")

            hospital.book_appointment(patient_id, doctor_id, date_only, twelve_hr_time)  # Calling the book appointment method from hospital system class

        elif selection == "CA":
            while True:
                appointment_id = input("Enter appointment ID: ").strip()
                if appointment_id:                                              # Error validation if nothing is selected
                    break
                else:
                    print("Appointment ID is empty. Please enter ID.")
            hospital.cancel_appointment(appointment_id)             # Calling the cancel appointment method from hospital system class
            app.cancel                                      # Calling the cancel method from appointment class

        elif selection == "PP":
            while True:
                patient_id = input("Enter Patient ID: ").strip()
                if patient_id:                                                 # Error validation if nothing is selected
                    break
                else:
                    print("Patient ID is empty. Please enter ID.")

            patient = hospital.patient.get(patient_id)          # Object of the hospital system class
            if patient:
                patient.view_profile()
            else:
                print("Unable to retrieve patient information")

        elif selection == "DP":
            doctor_id = input("\nEnter Doctor ID: ").strip()
            doctor = hospital.doctor.get(doctor_id)                  # Object of the hospital system class
            if doctor:

                print(f"\n Doctor speciality: {doctor.speciality}")
                print(f" Doctor age:     {doctor.age}")
                print(f" Doctor gender:   {doctor.gender}")
                print(f" Doctor ID:     {doctor.doctor_id}\n")
                doctor.view_schedule()                  # Calling the view schedule method from doctor class

            else:
                print("Unable to retrieve doctor information")

        elif selection == "GB":
            appointment_id = input("Enter appointment ID: ").strip()
            hospital.generate_bill(appointment_id)              # Calling the generate bill method from hospital class

        elif selection == "EX":
            print("Logging off.")
            break
        else:
            print("Oops! That selection isn’t valid. Pick a different one from menu.")


if __name__=="__main__":
    main_menu()
















