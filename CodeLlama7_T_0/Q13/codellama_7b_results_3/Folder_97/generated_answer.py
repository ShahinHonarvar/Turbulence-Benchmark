
def find_second_largest_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return None

    # Find the largest element in the list
    largest = max(my_list)

    # Find the second largest element in the list
    second_largest = None
    for i in range(40, 81):
        if my_list[i] > largest:
            continue

        if my_list[i] > second_largest or second_largest is None:
            second_largest = my_list[i]

    # Return the second largest element
    return second_largest
