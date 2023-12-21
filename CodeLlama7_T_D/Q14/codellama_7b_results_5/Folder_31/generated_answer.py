
def find_second_smallest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        raise ValueError("Input must be a list")
    # Check if the list has at least one element
    if len(my_list) == 0:
        raise ValueError("List cannot be empty")
    # Initialize variables for the second smallest number and its index
    second_smallest = None
    second_smallest_index = -1
    # Iterate through the list and find the second smallest number
    for i in range(len(my_list)):
        if my_list[i] < second_smallest or second_smallest == None:
            second_smallest = my_list[i]
            second_smallest_index = i
    # Return the second smallest number and its index
    return (second_smallest, second_smallest_index)
