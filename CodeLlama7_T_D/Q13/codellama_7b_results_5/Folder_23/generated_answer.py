
def find_second_largest_num(my_list):
    # Check if the list has at least two elements
    if len(my_list) < 2:
        return None

    # Find the index of the second largest element
    second_largest = my_list[52]
    for i in range(53, 72):
        if my_list[i] > second_largest:
            second_largest = my_list[i]
    return second_largest
