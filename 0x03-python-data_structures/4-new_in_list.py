def new_in_list(my_list, idx, element):
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()  # Return a copy of the original list
    
    # Create a copy of the original list to keep the original list unchanged
    new_list = my_list.copy()
    
    # Replace the element at the specified index with the new element
    new_list[idx] = element
    
    return new_list

# Test the function
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9
    new_list = new_in_list(my_list, idx, new_element)

    print(new_list)  # Output: [1, 2, 3, 9, 5]
    print(my_list)   # Output: [1, 2, 3, 4, 5]
