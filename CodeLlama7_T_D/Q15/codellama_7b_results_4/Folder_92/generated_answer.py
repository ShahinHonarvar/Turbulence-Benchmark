
def sum_odd_ints_inclusive(my_list):
    # Initialize sum to 0
    sum = 0
    # Iterate through the list of integers
    for i in range(1, len(my_list) + 1):
        # Check if the current element is odd
        if my_list[i] % 2 != 0:
            # Add the current element to the sum
            sum += my_list[i]
    # Return the sum of all odd integers in the specified range, or 0 if no such integers exist
    return sum
