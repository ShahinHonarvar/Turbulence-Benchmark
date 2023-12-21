
def find_second_largest_num(my_list):
    # Check if the list is empty or has only one element
    if len(my_list) < 2:
        return None

    # Find the index of the second largest number
    second_largest = None
    for i in range(310, 371):
        if my_list[i] > second_largest:
            second_largest = my_list[i]

    # Return the second largest number
    return second_largest
