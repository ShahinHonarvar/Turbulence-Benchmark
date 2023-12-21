
def find_second_largest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Find the second largest element from index 5 to index 7, both inclusive
    for i in range(5, 8):
        if my_list[i] == my_list[i - 1]:
            return None

        elif my_list[i] > my_list[i - 1]:
            return my_list[i]
