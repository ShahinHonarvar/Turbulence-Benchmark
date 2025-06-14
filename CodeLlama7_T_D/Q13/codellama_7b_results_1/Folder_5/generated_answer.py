
def find_second_largest_num(my_list):
    # Check if the input list is valid
    if not my_list or len(my_list) < 2:
        return None

    # Initialize variables for the second largest element and its index
    second_largest = None
    second_largest_index = -1

    # Iterate through the list and find the second largest element
    for i in range(len(my_list)):
        if my_list[i] > second_largest or second_largest == None:
            second_largest = my_list[i]
            second_largest_index = i

    # Return the second largest element from index 8 to index 9, both inclusive
    if second_largest_index >= 7 and second_largest_index <= 8:
        return second_largest

    else:

        return None
