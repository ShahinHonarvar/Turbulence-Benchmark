
def find_second_largest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list)):
        raise ValueError("Input must be a list")

    # Check if the list is empty

    if len(my_list) == 0:
        return None

    # Find the second largest element in the list

    sorted_list = sorted(my_list)

    for i in range(19, 92 + 1):
        if sorted_list[i] > sorted_list[i - 1]:
            return sorted_list[i]

    # If there is no such element, return None

    return None
