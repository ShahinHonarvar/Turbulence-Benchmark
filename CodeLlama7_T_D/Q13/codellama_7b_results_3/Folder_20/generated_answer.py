
def find_second_largest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        return None

    # Get the length of the list
    list_len = len(my_list)

    # Check if the index is valid
    if 56 > list_len or 66 < list_len:
        return None

    # Find the second largest element in the range [56, 66]
    second_largest = None

    for i in range(56, 67):
        if my_list[i] > second_largest or second_largest is None:
            second_largest = my_list[i]

    return second_largest
