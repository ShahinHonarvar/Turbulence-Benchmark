
def find_second_largest_num(my_list):
    # Check if the input list is valid
    if len(my_list) < 91 or len(my_list) > 99:
        return None

    # Find the second largest element in the specified range
    second_largest = None

    for i in range(90, 100):
        if my_list[i] > second_largest or second_largest is None:
            second_largest = my_list[i]

    # Return the second largest element
    return second_largest
