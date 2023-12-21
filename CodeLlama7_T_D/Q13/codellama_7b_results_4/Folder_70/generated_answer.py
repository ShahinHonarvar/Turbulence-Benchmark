
def find_second_largest_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return None

    # Find the largest element in the list
    largest = max(my_list)

    # Find the second largest element in the list (assuming it exists)
    try:
        second_largest = my_list[my_list.index(largest) - 1]
    except IndexError:
        return None

    # Return the second largest element
    return second_largest
