
def all_ints_div_by_both_two_nums(my_list):
    # Define the range of indices for which we want to find divisible integers
    start = 34
    end = 81
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate over the specified range of indices
    for i in range(start, end + 1):
        # Check if the current element is divisible by both 27 and 57
        if my_list[i] % 27 == 0 and my_list[i] % 57 == 0:
            # If it is divisible, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both 27 and 57 from index 34 to index 81, both inclusive
    return divisible_ints
