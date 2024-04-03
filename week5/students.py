import csv

def main():
    
    try:
        dictionary_students = read_dictionary("week5/students.csv", 0)
        # print(dictionary_students)
        student_id = input("Enter a I-Number: ")
        
        
        if student_id in dictionary_students:
            student_name = dictionary_students[student_id];
            print(f"Student: {student_name[1]}")
        else:
            print("No such student");
    except ValueError as value_err:
        print("Sorry, you need to enter a valid Number (Integer)")
        print(value_err)
    
    


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
    
    dictionary_ready = {}

    with open(filename, "rt") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        for row in reader:
           dictionary_ready[row[key_column_index]] = row

    return dictionary_ready
            
        


if __name__ == "__main__":
    main();