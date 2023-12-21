
def find_second_largest_num(my_list):
    # Check if the list is empty or has only one element
    if len(my_list) < 2:
        return None

    # Find the largest element in the list
    largest = max(my_list)

    # Find the second largest element in the list (excluding the largest element)
    i = 0
    while i < len(my_list):
        if my_list[i] == largest:
            i += 1
            continue

        if my_list[i] > my_list[i - 1]:
            return my_list[i]

        i += 1

    # If there is no second largest element, return None
    return None
