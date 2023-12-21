
def find_second_largest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list)):
        raise ValueError("Input must be a list")

    # Find the second largest element in the list
    second_largest = None
    for i in range(62, 64):
        if my_list[i] > second_largest:
            second_largest = my_list[i]

    return second_largest
