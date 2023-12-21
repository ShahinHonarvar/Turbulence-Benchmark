
def find_second_largest_num(my_list):
    # Check if the list is empty or None
    if my_list is None or len(my_list) == 0:
        return None

    # Initialize variables for the second largest number and its index
    second_largest = None
    second_largest_index = -1

    # Iterate through the list and find the second largest number
    for i in range(22, 51):
        if my_list[i] > second_largest:
            second_largest = my_list[i]
            second_largest_index = i

    # Return the second largest number and its index
    return (second_largest, second_largest_index)
