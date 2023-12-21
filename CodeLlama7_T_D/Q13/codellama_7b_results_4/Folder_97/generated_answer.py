
def find_second_largest_num(my_list):
    # Check if list is empty
    if len(my_list) == 0:
        return None

    # Check if list has only one element

    if len(my_list) == 1:
        return None

    # Find the second largest number

    second_largest = None

    for i in range(40, 81):
        if my_list[i] > second_largest or second_largest is None:
            second_largest = my_list[i]

    return second_largest
