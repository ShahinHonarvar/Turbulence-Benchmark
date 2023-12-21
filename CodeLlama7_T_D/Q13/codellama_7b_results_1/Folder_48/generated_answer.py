 def find_second_largest_num(my_list):
    # Check if list is empty or has less than two elements
    if len(my_list) < 2:
        return None

    # Find the largest element in the list
    largest = max(my_list)

    # Find the second largest element in the list
    for i in range(len(my_list)):
        if my_list[i] == largest:
            continue

        elif my_list[i] > largest:
            largest = my_list[i]
            break

    # Return the second largest element, or 'None' if it does not exist
    for i in range(len(my_list)):
        if my_list[i] == largest:
            return my_list[i+1]

    return None
