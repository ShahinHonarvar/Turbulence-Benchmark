
def find_second_largest_num(my_list):
    # Check if the list has at least two elements
    if len(my_list) < 2:
        return None

    # Find the second largest element in the list
    # by comparing each element with its successor
    second_largest = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] > second_largest:
            second_largest = my_list[i]

    # Return the second largest element
    return second_largest
