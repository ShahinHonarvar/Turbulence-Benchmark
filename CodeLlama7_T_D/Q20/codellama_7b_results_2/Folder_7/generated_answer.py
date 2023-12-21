 def find_n_th_smallest_num(my_list):
    # Find the nth smallest number in a list of distinct numbers
    # If the input is not a list, return an error message
    if type(my_list) != list:
        return "Error: Input must be a list."
    # If the list is empty, return an error message
    if len(my_list) == 0:
        return "Error: List cannot be empty."
    # Sort the input list in ascending order
    my_list.sort()
    # Return the 9th smallest number from index 470 to index 654, both inclusive
    return my_list[470:654+1].index(my_list[470:654+1][-1]) + 470
