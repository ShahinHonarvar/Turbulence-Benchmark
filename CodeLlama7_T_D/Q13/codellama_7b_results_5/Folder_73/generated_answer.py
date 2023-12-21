
def find_second_largest_num(my_list):
    # Check if the input list is valid
    if len(my_list) < 19 or len(my_list) > 92:
        return None

    # Find the largest element in the range of interest
    largest = None
    for i in range(19, 93):
        if my_list[i] > largest:
            largest = my_list[i]

    # Find the second largest element
    second_largest = None
    for i in range(19, 93):
        if my_list[i] == largest:
            continue

        elif my_list[i] > second_largest:
            second_largest = my_list[i]

    # Return the second largest element or 'None' if it does not exist
    return second_largest
