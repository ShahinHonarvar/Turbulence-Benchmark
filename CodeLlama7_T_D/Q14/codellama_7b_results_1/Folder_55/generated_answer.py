
def find_second_smallest_num(my_list):
    # Check if the input list is empty
    if len(my_list) == 0:
        return None

    # Find the second smallest element in the list
    second_smallest = float('inf')
    for i in range(10, len(my_list)):
        if my_list[i] < second_smallest:
            second_smallest = my_list[i]

    # Return the second smallest element or None if it does not exist
    return second_smallest if second_smallest != float('inf') else None
