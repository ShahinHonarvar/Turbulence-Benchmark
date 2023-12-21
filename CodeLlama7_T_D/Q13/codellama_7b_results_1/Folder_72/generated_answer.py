
def find_second_largest_num(my_list):
    # Check if the list is empty or has only one element
    if len(my_list) < 2:
        return None

    # Find the largest element in the list
    largest = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] > largest:
            largest = my_list[i]

    # Find the second largest element in the list
    second_largest = None
    for i in range(len(my_list)):
        if my_list[i] == largest:
            continue

        if (second_largest is None) or (my_list[i] > second_largest):
            second_largest = my_list[i]

    # Return the second largest element from index 29 to index 51, both inclusive
    if (second_largest is not None) and (29 <= len(my_list)) and (len(my_list) <= 51)):
        return second_largest

    # If there is no such element or the list is empty or has only one element, return 'None'
    return None
