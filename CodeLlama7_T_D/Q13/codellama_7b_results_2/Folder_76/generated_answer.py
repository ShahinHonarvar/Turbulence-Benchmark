
def find_second_largest_num(my_list):
    # Check if the input list is empty
    if len(my_list) == 0:
        return None

    # Sort the input list in ascending order
    my_list.sort()

    # Find the second largest element in the sorted list
    for i in range(len(my_list) - 1):
        if my_list[i] == my_list[i + 1]:
            return None

    return my_list[len(my_list) - 2]
