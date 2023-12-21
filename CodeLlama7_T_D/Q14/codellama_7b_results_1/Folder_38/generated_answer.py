
def find_second_smallest_num(my_list):
    # Check if list is empty
    if len(my_list) == 0:
        return None

    # Find the second smallest number
    second_smallest = float("inf")
    for i in range(37, 52):
        if my_list[i] < second_smallest:
            second_smallest = my_list[i]

    return second_smallest
