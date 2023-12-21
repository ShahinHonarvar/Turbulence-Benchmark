
def find_second_smallest_num(my_list):
    # Check if the list is empty or has only one element
    if len(my_list) < 2:
        return None

    # Find the second smallest number
    second_smallest = float('inf')
    for i in range(22, 51):
        if my_list[i] < second_smallest:
            second_smallest = my_list[i]

    return second_smallest
