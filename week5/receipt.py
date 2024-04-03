import csv
from datetime import datetime


# My "Exceeding the Requirements":
# Write code to discount the product prices by 10% 
# if today is Tuesday or Wednesday.

# I created a function: calculate_discount();

PRODUCT_NAME = 1
PRODUCT_CODE = 0
PRODUCT_PRICE = 2

def main():
    try:
        products_dict = read_dictionary("week5/products.csv", 0)
        request_list = read_list("week5/request.csv");
    
        current_date_and_time = datetime.now()
        total_items = 0
        subtotal = 0
    
        # print(f"{products_dict}")
        print("Inkom Emporium")
        print()
    
        for request in request_list:
            if request[0] in products_dict:
                product = products_dict[request[0]]
                print(f"{product[PRODUCT_NAME]}: {request[1]} @ {product[PRODUCT_PRICE]}")
            
                total_items += int(request[1])
                subtotal += float(product[PRODUCT_PRICE]) * float(request[1])
        print()  
        print(f"Number of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        tax = subtotal * 0.06;
        print(f"Sales Tax : {tax:.2f}")
        total_with_taxh = tax + subtotal;
        
        total = calculate_discount(total_with_taxh, current_date_and_time);
            
        print(f"Total: {total:.2f}")  
        print()
        print("Thank you for shopping at the Inkom Emporium.");
        print(f"{current_date_and_time:%a %b %d %H:%M:%S %Y}");
        
    except FileNotFoundError as not_found_err:
        print("Error: missing file");
        print(f"{not_found_err}");

    except PermissionError as permmission_err:
        print(f"{permmission_err}");
        
    except KeyError as key_err:
        print("Error: unknown product ID in the request.csv file");
        print(f"{key_err}");  

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary_products = {};
    
    with open(filename, "rt") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        
        for row in reader:
           dictionary_products[row[key_column_index]] = row;
           
    return dictionary_products;
    
    
def read_list(filename):
        list_request = [];
    
        with open(filename, "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)
        
            for row in reader:
                list_request.append(row);
           
        return list_request;
    
    
def calculate_discount(total, date):
    
    weekday_discounts = {
        1: 0.1,  # Tuesday
        2: 0.1   # Wednesday
    }
    weekday = date.weekday();
    
    if weekday in weekday_discounts:
        discount = total * weekday_discounts[weekday];
        total -= discount;
        print(f"Great! You received a discount of 10% ({discount:.2f})");
        
    return total;
    
if __name__ == "__main__":
    main();
