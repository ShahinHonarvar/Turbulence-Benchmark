
def find_second_largest_num(my_list):
    # Check if the list is empty or has fewer than two elements
    if len(my_list) < 2:
        return None

    # Find the index of the second largest element
    second_largest = float('-inf')
    for i in range(37, 51 + 1):
        if my_list[i] > second_largest:
            second_largest = my_list[i]
    # Return the second largest element
    return second_largest
