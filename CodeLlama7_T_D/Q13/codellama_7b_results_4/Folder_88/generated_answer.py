
def find_second_largest_num(my_list):
    # Check if list is empty
    if len(my_list) == 0:
        return None

    # Get the second largest element from index 4 to index 8, both inclusive
    second_largest = None
    for i in range(4, 9):
        if my_list[i] > second_largest or second_largest is None:
            second_largest = my_list[i]

    # Return the second largest element

    return second_largest
