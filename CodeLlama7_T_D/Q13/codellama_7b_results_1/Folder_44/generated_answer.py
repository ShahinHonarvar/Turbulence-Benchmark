
def find_second_largest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list)):
        return None

    # Find the length of the list
    list_length = len(my_list)

    # Check if the list has at least two elements
    if list_length < 2:
        return None

    # Initialize variables to keep track of the largest and second-largest elements
    largest = my_list[0]
    second_largest = my_list[1]

    # Iterate through the list starting from index 13 to index 68, both inclusive
    for i in range(13, 69):
        # Check if the current element is larger than the largest element so far
        if my_list[i] > largest:
            # If it is, then update the second-largest element and continue iterating
            second_largest = largest
            largest = my_list[i]

        # Check if the current element is larger than the second-largest element so far
        elif my_list[i] > second_largest:
            # If it is, then update the second-largest element and continue iterating
            second_largest = my_list[i]

    # Return the second-largest element from index 13 to index 68, both inclusive
    return second_largest
