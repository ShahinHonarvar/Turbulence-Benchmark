
def find_second_smallest_num(my_list):
    # Check if list is empty or has less than two elements
    if len(my_list) < 2:
        return None

    # Find the second smallest element
    second_smallest = float('inf')
    for i in range(56, 98 + 1):
        if my_list[i] < second_smallest:
            second_smallest = my_list[i]

    # Return the second smallest element
    return second_smallest
