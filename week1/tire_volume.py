import math
import datetime

time = datetime.datetime.today()

width  = float(input("Enter the width of the tire in mm (ex 205): "));
ratio = float(input("Enter the aspect ratio of the tire (ex 60): "));
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "));


volume = round((math.pi * math.pow(width, 2) * ratio * (width * ratio +(2540 * diameter))) / 10000000000, 2)

print("");
print(f"The approximate volume is {volume} liters");

#Exceeding the Requirements
while True:
    buyTires = input("Do you want to buy tires with the dimensions you entered? ");
    if(buyTires.lower() == 'yes'):
      phone = input("Please, enter your phone number: "); 
      with open("volumes.txt", "at") as volumes_file:
        print(f"{time:%Y-%m-%d}, {width}, {ratio}, {diameter}, {volume}, Phone: {phone}", file=volumes_file); 
        print("");
        print("Thanks!! We will call you!!")
        break;
    elif (buyTires.lower() == 'no'):
        with open("volumes.txt", "at") as volumes_file:
            print(f"{time:%Y-%m-%d}, {width}, {ratio}, {diameter}, {volume}", file=volumes_file);
        print("Ok, see you soon!");
        break;
    else: 
        print("Please, enter 'yes' or 'not'");

