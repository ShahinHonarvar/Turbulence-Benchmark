
def find_second_largest_num(my_list):
    # Check if the input list has at least two elements
    if len(my_list) < 2:
        return None

    # Find the index of the second largest element
    second_largest = None
    for i in range(43, 51 + 1):
        if my_list[i] > second_largest or second_largest is None:
            second_largest = my_list[i]

    # Return the second largest element
    return second_largest
