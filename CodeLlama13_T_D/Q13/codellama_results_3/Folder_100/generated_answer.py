
def find_second_largest_num(my_list):
    # Get the second largest element from index 42 to index 68, both inclusive
    second_largest = my_list[42:69][-2]
    
    # If there is no such element, return None
    if not second_largest:
        return None
    
    # Otherwise, return the second largest element
    return second_largest
