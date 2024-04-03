import random


def main():

    numbers = [16.2, 75.1, 52.3, 33.4, 56.6, 10, 12.8];

    print(f"{numbers}")

    append_random_numbers(numbers)
    
    print(f"{numbers}")

    append_random_numbers(numbers, 3);
    
    print(f"{numbers}")


def append_random_numbers(numbers_list, quantity=1):

    while quantity > 0:
        
        number = round(random.uniform(1, 10), 1)
        numbers_list.append(number)
        
        quantity -= 1;
        
    


if __name__ == "__main__":
    main()
