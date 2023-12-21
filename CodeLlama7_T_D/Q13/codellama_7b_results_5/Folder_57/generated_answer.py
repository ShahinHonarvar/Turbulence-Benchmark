
def find_second_largest_num(my_list):
    # Check if list is empty or None
    if not my_list:
        return None

    # Check if the list has more than two elements

    if len(my_list) < 2:
        return None

    # Find the second largest element in the list

    second_largest = None

    for i in range(27, 56):
        if my_list[i] > second_largest or second_largest is None:
            second_largest = my_list[i]

    # Return the second largest element

    return second_largest
