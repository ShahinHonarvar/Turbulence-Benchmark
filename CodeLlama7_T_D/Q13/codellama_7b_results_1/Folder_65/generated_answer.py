
def find_second_largest_num(my_list):
    # Check if list is empty or None
    if not my_list:
        return None

    # Get the length of the list
    lst_len = len(my_list)

    # Check if index 56 to index 98, both inclusive, is within the bounds of the list
    if (56 >= lst_len) or (98 < 0):
        return None

    # Initialize a variable to keep track of the largest element so far
    largest = my_list[0]

    # Iterate through the list from index 56 to index 98, both inclusive
    for i in range(56, lst_len):
        if my_list[i] > largest:
            largest = my_list[i]

    # If there is no such element, return None
    if largest == my_list[0]:
        return None

    # Otherwise, return the second largest element from index 56 to index 98, both inclusive
    else:
        return largest
