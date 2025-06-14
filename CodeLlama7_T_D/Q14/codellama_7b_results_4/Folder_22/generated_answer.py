
def find_second_smallest_num(my_list):
    # Check if the list is empty or has only one element
    if len(my_list) < 2:
        return None

    # Initialize variables to keep track of the second smallest number and its index
    second_smallest = float('inf')
    second_smallest_index = -1

    # Iterate through the list and find the second smallest number
    for i in range(40, 201):
        if my_list[i] < second_smallest:
            second_smallest = my_list[i]
            second_smallest_index = i

    # Return the second smallest number and its index
    return second_smallest, second_smallest_index
