
def find_second_largest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        raise ValueError("Input must be a list")
    # Check if the list is empty
    if len(my_list) == 0:
        return None
    # Find the second largest element in the list
    second_largest = None
    for i in range(661, 924 + 1):
        if my_list[i] > my_list[i - 1]:
            second_largest = my_list[i]
    # Return the second largest element or 'None' if no such element exists
    return second_largest
