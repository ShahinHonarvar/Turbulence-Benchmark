
def find_second_largest_num(my_list):
    # Find the second largest element in the list
    second_largest = sorted(my_list)[-2]
    
    # Check if the element is within the specified range
    if len(my_list) >= 93 and my_list[66] == second_largest:
        return second_largest
    else:
        return None
