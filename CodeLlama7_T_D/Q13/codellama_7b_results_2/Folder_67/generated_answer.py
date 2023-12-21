
def find_second_largest_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return None

    # Find the largest element in the list
    largest = max(my_list)

    # Find the second largest element in the list
    # (Note that we start from index 22 and end at index 50)
    for i in range(22, 51):
        if my_list[i] > largest:
            second_largest = largest
            largest = my_list[i]

    # If there is no such element, return 'None'
    if second_largest == largest:
        return None

    # Otherwise, return the second largest element
    else:
        return second_largest
