
def sum_odd_ints_inclusive(my_list):
    # Initialize variables
    sum = 0
    start_index = 209
    end_index = 556
    # Iterate through list from start to end index
    for i in range(start_index, end_index + 1):
        # Check if current element is an odd integer
        if my_list[i] % 2 != 0:
            # Add current element to sum
            sum += my_list[i]
    # Return sum
    return sum
