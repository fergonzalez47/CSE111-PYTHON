def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    
    fruit_list.reverse();
    print(f"Reversed: {fruit_list}")
    
    
    fruit_list.append("orange");
    print(f"orange: {fruit_list}")
    
    i = fruit_list.index("apple");
    fruit_list.insert(i, "cherry");
    
    fruit_list.remove("banana");
    print(f"BANANA REMOVED: {fruit_list}")
    
    poped = fruit_list.pop()
    print(f"removed {poped}" )
    print(fruit_list)
    
    fruit_list.sort()
    print(f"Sorted: {fruit_list}")
    fruit_list.clear()
    print(f"Clear method: {fruit_list}")
    
    
    
    
    
if __name__ == "__main__":
    main();
