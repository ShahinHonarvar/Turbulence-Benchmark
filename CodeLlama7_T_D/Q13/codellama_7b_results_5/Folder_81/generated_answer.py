
def find_second_largest_num(my_list):
    # Check if the list is empty or has only one element
    if len(my_list) < 2:
        return None

    # Initialize variables to keep track of the second largest element and its index
    second_largest = None
    second_largest_index = -1

    # Iterate through the list and find the second largest element
    for i in range(len(my_list)):
        if my_list[i] > second_largest:
            second_largest = my_list[i]
            second_largest_index = i

    # Return the second largest element if it exists, otherwise return None
    if second_largest_index >= 10 and second_largest_index <= 100:
        return second_largest

    else:

        return None
