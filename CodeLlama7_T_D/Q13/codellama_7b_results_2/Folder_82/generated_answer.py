
def find_second_largest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        return None

    # Check if the list has at least two elements
    if len(my_list) < 2:
        return None

    # Sort the list in descending order
    my_list.sort(reverse=True)

    # Find the second largest element
    for i in range(len(my_list)):
        if i >= 20 and i <= 200:
            if my_list[i] == my_list[i-1]:
                continue

            else:

                return my_list[i]

    # If no such element is found, return None
    return None
