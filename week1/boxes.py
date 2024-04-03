import math

items = int(input("Number of manufactured items: "))

itemsPerBox = int(input("How many items do you want to pack per box? : "))


result = math.ceil(items / itemsPerBox);

print (f"Number of boxes that you need: {result}");

