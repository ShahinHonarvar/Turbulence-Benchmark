
def all_odd_ints_exclusive(my_list):
    # Create an empty list to store the results
    result = []

    # Iterate through the list of integers, starting from index 3
    for i in range(3, len(my_list)):

        # Check if the current element is odd
        if my_list[i] % 2 != 0:

            # If it is, add it to the results list
            result.append(my_list[i])

    # Return the results list
    return result
