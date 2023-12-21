
def find_second_largest_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return None

    # Find the largest element in the list
    largest = max(my_list)

    # Find the second largest element in the list
    second_largest = None
    for i in range(len(my_list)):
        if my_list[i] > largest and my_list[i] < second_largest or second_largest is None:
            second_largest = my_list[i]

    # Return the second largest element from index 75 to index 85, both inclusive
    if second_largest is not None and (75 <= second_largest <= 85):
        return second_largest

    # If there is no such element, return 'None'
    return None
