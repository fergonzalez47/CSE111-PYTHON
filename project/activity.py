import tkinter as tk
from tkinter import Entry, Frame, Label, Button, ttk
from number_entry import FloatEntry
from str_entry import StringEntry

import requests

from utils import *
from utils import string_to_lowercase



def main():

    root = tk.Tk();

    frm_main = Frame(root)
    frm_main.master.title("Phisical Activity App")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)
    
    populate_main_window(frm_main)


    root.mainloop()


def show_hiking_frame(label):

    def set_difficult(event=None):
        try:
            selected_option = combo.get()
            difficulty_value = 0

            if selected_option == "Easy":
               difficulty_value = 4
            elif selected_option == "Moderate":
                difficulty_value = 3.5
            elif selected_option == "Difficult":
                difficulty_value = 3
            elif selected_option == "Very Difficult":
                difficulty_value = 2.5

            division()

        except Exception as excep:
            error_message_difficulty.config(text=f"{excep}")

        return float(difficulty_value)

    lbl_difficulty = Label(label, text="Difficulty:",
    font=("Helvetica", 12))
    difficulty = ["Very Difficult", "Difficult", "Moderate", "Easy"]
    combo = ttk.Combobox(label, values=difficulty)
    combo.set("Select the difficult")

    # field to show an error message in case the error exists
    error_message_difficulty = Label(label, text="", fg="red");

    lbl_instruction = Label(
        label, text="Please enter the distance of the hiking route in Km (Example: 14 (km)")
    ent_distance = FloatEntry(label, width=4, lower_bound=0, upper_bound=900)
    lbl_hrs = Label(label, text="Hours (aprox)")

    lbl_time = Label(label, text="Approximate time to complete the route: ")
    lbl_result = Label(label, width=3, fg="green", font=("helvetica", 12))
    lbl_pdt = Label(label, text="", wraplength=300, fg="gray")
    lbl_instruction.grid(row=0, column=0, padx=3, pady=3)
    ent_distance.grid(row=1, column=0, padx=1, pady=1)

    lbl_time.grid(row=4, column=0, padx=3, pady=3)
    lbl_difficulty.grid(row=2, column=0, padx=3, pady=3)
    combo.grid(row=3, column=0, padx=2, pady=0)
    error_message_difficulty.grid(row=5, column=0, padx=0, pady=3)

    lbl_hrs.grid(row=4, column=2, padx=3, pady=3)
    lbl_result.grid(row=4, column=1, padx=3, pady=3)
    lbl_pdt.grid(row=5, column=0, padx=3, pady=3)

    def division(event=None):
        try:
            difficulty_value = set_difficult();

            if difficulty_value != 0:

                error_message_difficulty.config(text="")

                distance = float(ent_distance.get())
                total = round(distance / difficulty_value, 2)
                lbl_result.config(text=f"{total}")
                lbl_pdt.config(
                    text="Remember, this is just an estimation, and the actual time may vary depending on terrain conditions, the walker's physical condition, and other factors.")

            else:
                error_message_difficulty.config(
                    text="You need to select the difficulty!")

        except ValueError:
            lbl_result.config(text="Invalid input")

    ent_distance.bind("<KeyRelease>", division)
    combo.bind("<<ComboboxSelected>>", set_difficult)


def show_surf_frame(label):
    lbl_city = Label(label, text="Enter the city where you will be surfing: ")
    ent_city = Entry(label)
    lbl_city_error = Label(label, text="", fg="red")

    btn_get_info = Button(label, text="Get Information")

    lbl_result = Label(label, text="", font=("helvetica", 11), fg="blue")

    # Configurar la disposición de los widgets usando el método grid
    lbl_city.grid(row=0, column=0, padx=3, pady=3, sticky="e")
    ent_city.grid(row=0, column=1, padx=3, pady=3)
    btn_get_info.grid(row=1, column=0, columnspan=2, padx=3, pady=3)
    lbl_city_error.grid(row=2, column=0, columnspan=2, padx=3, pady=3)
    lbl_result.grid(row=3, column=0, columnspan=2, padx=3, pady=3)

    def get_inf_city():
        try:
            city = ent_city.get()
            if city.strip():
                city_name = string_to_lowercase(city)
                url = f"https://wttr.in/{city_name}?format=j1"
                res = requests.get(url)

                if res.status_code == 200:
                    city_dict = res.json()
                    temp_c = city_dict["current_condition"][0]["temp_C"]
                    temp_f = city_dict["current_condition"][0]["temp_F"]
                    local_time = city_dict["current_condition"][0]["localObsDateTime"]
                    humidity = city_dict["current_condition"][0]["humidity"]
                    wind_dir_degree = city_dict["current_condition"][0]["winddirDegree"]
                    wind_speed_kmh = city_dict["current_condition"][0]["windspeedKmph"]
                    inf = city_dict["current_condition"][0]["weatherDesc"][0]["value"]
                    country = city_dict["nearest_area"][0]["country"][0]["value"]
                    area_name = city_dict["nearest_area"][0]["areaName"][0]["value"]

                    lbl_city_error.config(text="")
                    lbl_result.config(text=f"{area_name:}\n Country: {country} \n Inf: {inf} \n Temperature C° = {temp_c}° \n Temperature F° ={temp_f}° \n Zone Time: { local_time} \n Humidity: {humidity} \n Wind dir. degree: {wind_dir_degree} ° \n Wind speed(km/h): {wind_speed_kmh} Km/h")
                    print(f"{area_name:}\n Country: {country} \n Inf: {inf} \n Temperature C° = {temp_c}° \n Temperature F° ={temp_f}° \n Zone Time: { local_time} \n Humidity: {humidity} \n Wind dir. degree: {wind_dir_degree} ° \n Wind speed(km/h): {wind_speed_kmh} Km/h")
                else:
                    lbl_result.config(text="Failed to fetch weather data")
            else:
                lbl_city_error.config(text="Please enter a valid city")
        except ValueError as val_err:
            lbl_city_error.config(text=f"Value error: {val_err}")
        except TypeError as type_error:
            lbl_city_error.config(text=f"Type error: {type_error}")
        except Exception as exception:
            print(exception)
            lbl_city_error.config(text=str(exception))

    btn_get_info.config(command=get_inf_city)


def show_jogging_frame(label):

    def set_weight_units(event=None):
        try:
            selected_option = combo.get()
            weight_units = ""

            if selected_option == "kilograms":
               weight_units = "KG"
            elif selected_option == "Pounds":
                weight_units = "LB"


        except Exception as excep:
            error_message.config(text=f"{excep}")

        return weight_units


    units = ["kilograms", "Pounds"]
    combo = ttk.Combobox(label, values=units)
    combo.set("Select here")

    # field to show an error message in case the error exists
    error_message = Label(label, text="", fg="red")

    lbl_instruction = Label(
    label, text="Please enter the distance you jogged in km (Example: 2 km)")
   
    lbl_distance = Label(label, text="km")
    
    
    lbl_result = Label(label, text="", fg="green")
    ent_kcal = Label(label, text="")

    lbl_body_weight = Label(label, text="Enter your body weight: ")
    
    #ENTRIES
    ent_body_weight = Entry(
        label, width=4)
    ent_distance = Entry(label, width=4)
    
    
    #lbl calories / KG
    
    lbl_kilograms_lost_days = Label(label, text="")
    lbl_days = Label(label, text="Days (aprox)")
    lbl_kilograms_lost_days_message = Label(
        label, text="How many days would you lose 1 Kg based on if you burn the same amount of calories each day: ")
    
    #GRID
    lbl_instruction.grid(row=0, column=0, padx=1, pady=3)
    ent_distance.grid(row=1, column=0, padx=0, pady=3)
    lbl_distance.grid(row=1, column=1, padx=0, pady=3)
    lbl_result.grid(row=5, column=0, padx=1, pady=3)
    lbl_body_weight.grid(row=2, column=0, padx=3, pady=3)
    ent_body_weight.grid(row=3, column=0, padx=0, pady=3)
    combo.grid(row=3, column=1, padx=1, pady=3)
    
    lbl_kilograms_lost_days.grid(row=6, column=1, padx=1, pady=3)
    lbl_kilograms_lost_days_message.grid(row=6, column=0, padx=1, pady=3)
    lbl_days.grid(row=6, column=2, padx=1, pady=3)
    # lbl_for_weight_units.grid(row=2, column=0, padx=3, pady=3)
    error_message.grid(row=7, column=0, padx=3, pady=3, columnspan=2)
    ent_kcal.grid(row=4, column=2, padx=3, pady=3)
    
    def get_calculation():
        try:
            weight_units = set_weight_units()
            body_weight_str = ent_body_weight.get()
            distance_str = ent_distance.get()

            # Verificar si los campos de entrada no están vacíos
            if body_weight_str.strip() and distance_str.strip():
                body_weight = float(body_weight_str)
                distance = float(distance_str)

                if body_weight > 0 and distance > 0:
                    if weight_units:
                        lbl_result.config(text="")
                        error_message.config(text="")
                        result = calculate_calories(
                            body_weight, distance, weight_units)
                        lbl_result.config(text=result)
                        ent_kcal.config(text="Kcal (approx)")
                        
                        kgs_per_day = kilograms_lost(result)
                        lbl_kilograms_lost_days.config(text=kgs_per_day)
                    else:
                        error_message.config(
                            text="Please select the unit of weight measurement")
                else:
                    error_message.config(
                        text="Please enter valid numbers for body weight and distance")
            else:
                error_message.config(
                    text="Please fill out the fields")
        except ValueError as error:
            error_message.config(
                text="Please enter valid numbers for body weight and distance")
        except TypeError as type_error:
            error_message.config(
                text="Type error: Please fill out the fields correctly")
        except Exception as exception:
            print(exception)
            error_message.config(text=f"Exception: {exception}")

    
    
    btn_get_result = Button(label, text="Calculate")
    btn_get_result.grid(row=8, column=0, padx=3, pady=3, columnspan=2)
    btn_get_result.config(command=get_calculation)
    
    combo.bind("<<ComboboxSelected>>", set_weight_units)


# def show_weightlifting_frame(label):
#     pass




def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    
    """

    # Create a label that displays "Welcome:"
    lbl_welcome = Label(
        frm_main, text="Welcome! This is a program that will help you learn details about the physical activity you want to do, such as: Calories burned per activity, time it will take you to complete it, etc.",
        wraplength=700,
        font=("Helvetica", 14))

    lbl_welcome.config(fg="#093D67")

    lbl_options = Label(frm_main, text="Please, select the activity you want to do:",
    font=("Helvetica", 14))

    activities = ["Hiking", "Surf", "Jogging"]
    combo = ttk.Combobox(frm_main, values=activities)
    
    lbl_activity = tk.Label(frm_main, text="")
    lbl_activity.grid(row=5, column=0, padx=3, pady=3)
    # Layout the labels
    lbl_welcome.grid(row=0, column=0, padx=3, pady=3)
    lbl_options.grid(row=1, column=0, padx=3, pady=3)
    combo.grid(row=2, column=0, padx=3, pady=3)
    
    def activity_select(event):
        
        for widget in lbl_activity.winfo_children():
            widget.destroy()

        
        try:
            selected_option = combo.get()

            if selected_option == "Hiking":
                show_hiking_frame(lbl_activity)
                
            elif selected_option == "Surf":
                show_surf_frame(lbl_activity)
                
            elif selected_option == "Jogging":
                show_jogging_frame(lbl_activity)
                
            # elif selected_option == "Weightlifting":
            #     show_weightlifting_frame(lbl_activity)
                
                
        except Exception as excep:
            lbl_activity.config(text=f"{excep}")


    
    

    combo.set("Pick an Activity")
    
    combo.bind("<<ComboboxSelected>>", activity_select)
    
    
   

if __name__ == "__main__":
    main()