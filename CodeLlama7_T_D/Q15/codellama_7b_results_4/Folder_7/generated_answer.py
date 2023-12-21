
def sum_odd_ints_inclusive(my_list):
    # Initialize the sum variable
    sum = 0

    # Iterate through the list, starting from index 661 and ending at index 924 (inclusive)
    for i in range(661, 925):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the sum
            sum += my_list[i]

    # Return the final sum
    return sum
