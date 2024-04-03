import datetime

today = datetime.datetime.today().weekday();
print(today);

subtotal = float(input("Please enter the subtotal: "));

tax = subtotal * 0.06;
total = subtotal + tax;

if subtotal >= 50 and (today == 1 or today == 2):
    discount = round(subtotal * 0.1, 2);
    tax = (subtotal - discount) * 0.06;
    total = (subtotal - discount) + tax;
    print(f"Discount amount: {discount}");
elif subtotal <= 50 and (today == 1 or today == 2):
    amount = round(50 - subtotal,2);
    print(f"You need to need purchase ${amount} in order to receive the discount of 10%"); 

print(f"");
print(f"Sales tax amount: {round(tax, 2)}");
print(f"Total: {round(total, 2)}");
