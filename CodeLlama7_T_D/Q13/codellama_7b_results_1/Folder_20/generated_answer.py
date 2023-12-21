
def find_second_largest_num(my_list):
    # Check if list is empty or None
    if my_list is None or len(my_list) == 0:
        return None

    # Find the second largest element in the list
    second_largest = None
    for i in range(56, 67):
        if my_list[i] > second_largest:
            second_largest = my_list[i]

    return second_largest
