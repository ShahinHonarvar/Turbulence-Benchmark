
def find_second_largest_num(my_list):
    # Check if list is empty or None
    if not my_list:
        return None
    
    # Find the second largest element in the list
    second_largest = sorted(my_list)[-2]
    
    # Check if the second largest element is within the specified range (52 to 71)
    if my_list.index(second_largest) >= 52 and my_list.index(second_largest) <= 71:
        return second_largest
    
    # If the second largest element is not within the specified range, return None
    else:
        return None
