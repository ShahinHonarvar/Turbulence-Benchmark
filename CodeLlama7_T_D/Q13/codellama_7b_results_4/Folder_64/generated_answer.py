 def find_second_largest_num(my_list):
    # Check if list is empty
    if len(my_list) == 0:
        return None

    # Find the largest element in the list
    largest = max(my_list)

    # Find the second largest element in the list
    second_largest = None
    for i in range(len(my_list)):
        if my_list[i] > largest and my_list[i] != largest:
            second_largest = my_list[i]

    # Return the second largest element if it exists, otherwise return 'None'
    return second_largest
