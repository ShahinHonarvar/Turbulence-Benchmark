
def find_second_largest_num(my_list):
    # Find the largest element in the list
    largest = max(my_list)

    # Find the second largest element in the list (excluding the largest element)
    i = 0
    while i < len(my_list):
        if my_list[i] == largest:
            i += 1
            continue

        second_largest = my_list[i]
        i += 1

    # Return the second largest element (or None if it does not exist)
    return second_largest
