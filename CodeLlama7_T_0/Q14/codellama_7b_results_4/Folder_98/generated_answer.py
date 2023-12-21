
def find_second_smallest_num(my_list):
    # Check if the list is empty or has only one element
    if len(my_list) < 2:
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Initialize a variable to store the second smallest element
    second_smallest = None

    # Iterate through the list starting from index 6
    for i in range(5, len(my_list)):
        # Check if the current element is smaller than the previous smallest element
        if my_list[i] < my_list[i - 1]:
            # If it is, store it in the second_smallest variable
            second_smallest = my_list[i]

    # Return the second smallest element
    return second_smallest
