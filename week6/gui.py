import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry


def main():

    root = tk.Tk()
    frm_main = Frame(root)
    frm_main.master.title("Area of a rectangle")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    populate_main_window(frm_main)

    root.mainloop()


def populate_main_window(main):

    lbl_instruction = Label(main, text="Please, enter the width: ")
    ent_width = IntEntry(main, width=6, lower_bound=0)
    lbl_width_units = Label(main, text="cm")

    lbl_instruction_height = Label(main, text="Enter the height: ")
    ent_height = IntEntry(main, width=6, lower_bound=0)
    lbl_height_units = Label(main, text="cm")

    btn_calculate = Button(main, text="Calculate")

    lbl_instruction.grid(row=0, column=0, padx=3, pady=3)
    ent_width.grid(row=0, column=1, padx=3, pady=3)
    lbl_width_units.grid(row=0, column=2, padx=3, pady=3)

    lbl_instruction_height.grid(row=1, column=0, padx=3, pady=3)
    ent_height.grid(row=1, column=1, padx=3, pady=3)
    lbl_height_units.grid(row=1, column=2, padx=3, pady=3)

    btn_calculate.grid(row=2, column=1, padx=3, pady=3, columnspan=2)

    lbl_area = Label(main, text="Area:")
    lbl_area.grid(row=3, column=0, padx=3, pady=3)

    # Create label that will display the result.
    lbl_result = Label(main, width=10)
    lbl_result.grid(row=3, column=1, padx=3, pady=3)

    # Function to calculate area and update lbl_result
    def calculate_area():
        try:
            width = int(ent_width.get())
            height = int(ent_height.get())
            area = width * height
            lbl_result.config(text=str(area))
        except ValueError:
            lbl_result.config(text="Invalid Input")

    # Associate the calculate_area function with the button click event
    btn_calculate.config(command=calculate_area)


if __name__ == "__main__":
    main()
