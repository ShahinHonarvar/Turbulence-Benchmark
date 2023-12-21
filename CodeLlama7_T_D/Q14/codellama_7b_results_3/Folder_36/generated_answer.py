
def find_second_smallest_num(my_list):
    # Check if the input list is empty or None
    if not my_list:
        return None

    # Sort the input list in ascending order
    my_list.sort()

    # Initialize a variable to keep track of the second smallest element
    second_smallest = None

    # Iterate through the sorted list and find the second smallest element
    for i in range(len(my_list)):
        if my_list[i] != my_list[i - 1]:
            second_smallest = my_list[i]
            break

    return second_smallest
