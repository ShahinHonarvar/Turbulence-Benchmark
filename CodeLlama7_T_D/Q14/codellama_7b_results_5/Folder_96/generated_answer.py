
def find_second_smallest_num(my_list):
    # Check if list is empty or has only one element
    if len(my_list) < 2:
        return None

    # Get the smallest element and its index
    smallest = my_list[0]
    smallest_index = 0

    # Find the second smallest element and its index
    for i in range(1, len(my_list)):
        if my_list[i] < smallest:
            smallest = my_list[i]
            smallest_index = i

    # Return the second smallest element or None if it doesn't exist
    if smallest_index >= 50 and smallest_index <= 200:
        return my_list[smallest_index + 1]

    else:

        return None
