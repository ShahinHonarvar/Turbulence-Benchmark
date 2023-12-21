
def find_second_largest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        return None

    # Check if the list has at least two elements
    if len(my_list) < 2:
        return None

    # Find the second largest element in the list
    second_largest = None
    for i in range(len(my_list)):
        if my_list[i] > my_list[i - 1]:
            if second_largest == None:
                second_largest = my_list[i]
            elif my_list[i] > second_largest:
                second_largest = my_list[i]
    # Return the second largest element, or 'None' if it does not exist
    return second_largest
