
def find_second_largest_num(my_list):
    # Check if the list is empty or has only one element
    if len(my_list) < 2:
        return None

    # Find the largest element in the list
    largest = max(my_list)

    # Find the second largest element in the list (if it exists)
    for i in range(len(my_list)):
        if my_list[i] == largest:
            continue

        elif my_list[i] > largest:
            largest = my_list[i]

    # Return the second largest element (if it exists)
    return largest
