
def find_second_largest_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return None
    
    # Find the second largest element
    largest_num = my_list[99]
    for i in range(100, 200):
        if my_list[i] > largest_num:
            largest_num = my_list[i]
    
    # Return the second largest element
    return largest_num
