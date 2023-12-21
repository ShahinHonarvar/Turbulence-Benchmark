
def find_second_largest_num(my_list):
    # Find the largest element in the list
    largest = max(my_list)

    # Create a copy of the list without the largest element
    my_list = [x for x in my_list if x != largest]

    # Find the second largest element in the list
    second_largest = max(my_list)

    # Return the second largest element, or None if it does not exist
    if second_largest == largest:
        return None
    else:
        return second_largest
