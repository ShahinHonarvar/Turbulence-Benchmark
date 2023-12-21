
def find_second_largest_num(my_list):
    # Check if list is empty or has less than two elements
    if len(my_list) < 2:
        return None

    # Find the largest element in the list
    largest = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] > largest:
            largest = my_list[i]

    # Find the second largest element in the list
    second_largest = None
    for i in range(len(my_list)):
        if my_list[i] == largest:
            continue

        if (second_largest is None) or (my_list[i] > second_largest):
            second_largest = my_list[i]

    # Return the second largest element, or 'None' if it does not exist
    return second_largest
