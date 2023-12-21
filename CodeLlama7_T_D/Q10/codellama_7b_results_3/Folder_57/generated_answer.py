
def all_odd_ints_exclusive(my_list):
    # Create an empty list to store the result
    result = []

    # Iterate through the list of integers, starting from index 18 and ending at index 37 (both exclusive)
    for i in range(18, 37):
        # Check if the current element is odd
        if my_list[i] % 2 != 0:
            # If it is odd, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
