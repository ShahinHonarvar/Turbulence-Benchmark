
def find_second_smallest_num(my_list):
    # Check if the list has at least two elements
    if len(my_list) < 2:
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Initialize a variable to keep track of the second smallest element
    second_smallest = None

    # Iterate over the list and find the second smallest element
    for i in range(len(my_list)):
        if my_list[i] != my_list[i-1]:
            if second_smallest == None:
                second_smallest = my_list[i]
            else:
                return None

    # Return the second smallest element
    return second_smallest
