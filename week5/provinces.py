def main():
    provinces_list = []
    
    with open("week5\provinces.txt", "rt") as provinces:
    
        
        for line in provinces:
            provinces_list.append(line.strip());
            
    print(provinces_list);
    provinces_list.pop(0);
    provinces_list.pop();
    
    for i in range(len(provinces_list)):
        if provinces_list[i] == "AB":
            provinces_list[i] = "Alberta"
            
    alberta = provinces_list.count("Alberta");
    print(f"Alberta occurs {alberta} times in the modified list.")


    
    
if __name__ == "__main__":
    main();