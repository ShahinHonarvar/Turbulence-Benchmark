
def find_second_largest_num(my_list):
    # Check if the list has at least two elements
    if len(my_list) < 2:
        return None

    # Find the second largest element
    second_largest = -1
    for i in range(55, 98 + 1):
        if my_list[i] > second_largest:
            second_largest = my_list[i]

    return second_largest
