
def find_second_largest_num(my_list):
    # Sort the list in descending order
    my_list.sort(reverse=True)
    
    # Find the second largest element from index 12 to index 92, both inclusive
    for i in range(12, 93):
        if my_list[i] != my_list[i-1]:
            return my_list[i]
    
    # If there is no such element, return None
    return None
