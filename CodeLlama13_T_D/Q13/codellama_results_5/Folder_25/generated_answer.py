
def find_second_largest_num(my_list):
    # Find the largest element in the list
    largest = max(my_list)

    # Remove the largest element from the list
    my_list.remove(largest)

    # Find the second largest element in the remaining list
    second_largest = max(my_list)

    # Return the second largest element if it falls between indices 29 and 93, inclusive
    if 29 <= my_list.index(second_largest) <= 93:
        return second_largest

    # Otherwise, return None
    else:
        return None
