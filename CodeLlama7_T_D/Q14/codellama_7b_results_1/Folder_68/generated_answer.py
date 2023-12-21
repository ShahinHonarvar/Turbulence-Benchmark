
def find_second_smallest_num(my_list):
    # Check if the input list is empty
    if not my_list:
        return None

    # Sort the list and get the second smallest element
    sorted_list = sorted(my_list)
    second_smallest = None
    for i in range(len(sorted_list)):
        if sorted_list[i] != sorted_list[0]:
            second_smallest = sorted_list[i]
            break

    return second_smallest
