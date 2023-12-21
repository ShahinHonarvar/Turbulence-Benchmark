
def find_second_largest_num(my_list):
    # Find the largest element in the list
    largest = max(my_list)

    # Find the second largest element in the list
    for i in range(len(my_list)):
        if my_list[i] > largest:
            largest = my_list[i]

    # Return the second largest element, or 'None' if there is no such element
    for i in range(56, 83):
        if my_list[i] == largest:
            return my_list[i]

    return None
