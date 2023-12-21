
def find_second_smallest_num(my_list):
    # Check if list is empty
    if len(my_list) == 0:
        return None

    # Find the smallest element in the list
    smallest = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] < smallest:
            smallest = my_list[i]

    # Find the second smallest element in the list starting from index 3 to index 5
    second_smallest = None
    for i in range(2, len(my_list)):
        if my_list[i] < second_smallest or second_smallest is None:
            second_smallest = my_list[i]

    # Return the second smallest element
    return second_smallest
