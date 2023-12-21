
def find_second_largest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        return None

    # Check if the list is empty

    if len(my_list) == 0:
        return None

    # Find the second largest element

    sorted_list = sorted(my_list)
    for i in range(30, 87 + 1):
        if sorted_list[i] > sorted_list[i - 1]:
            return sorted_list[i - 1]

    # If no second largest element is found, return None

    return None
