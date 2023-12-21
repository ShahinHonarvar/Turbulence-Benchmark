
def find_second_largest_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return None

    # Find the second largest element
    second_largest = None
    for i in range(33, 37):
        if my_list[i] > second_largest or second_largest is None:
            second_largest = my_list[i]

    return second_largest
