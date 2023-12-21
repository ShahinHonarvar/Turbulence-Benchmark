
def find_second_largest_num(my_list):
    # Check if the list is empty or not
    if len(my_list) == 0:
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
        elif second_largest is None or my_list[i] > second_largest:
            second_largest = my_list[i]

    # Return the second largest element from index 75 to index 94, both inclusive

    start_index = 75
    end_index = 94
    for i in range(start_index, end_index + 1):
        if my_list[i] == second_largest:
            return my_list[i]

    # If there is no such element, the function should return 'None'

    return None
