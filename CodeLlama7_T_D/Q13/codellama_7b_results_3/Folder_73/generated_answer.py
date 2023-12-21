
def find_second_largest_num(my_list):
    # Check if the input list is empty or has only one element
    if len(my_list) < 2:
        return None

    # Find the largest element in the list
    largest = max(my_list)

    # Find the second largest element in the list
    # (note that we're skipping the largest element)
    second_largest = None
    for i in range(len(my_list)):
        if my_list[i] != largest:
            if second_largest == None or my_list[i] > second_largest:
                second_largest = my_list[i]

    # Return the second largest element in the list
    return second_largest
