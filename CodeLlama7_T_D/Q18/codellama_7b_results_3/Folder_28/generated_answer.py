
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables for the starting and ending indices of the range
    start = 34
    end = 81
    # Initialize an empty list to store the divisible integers
    divisible_ints = []
    # Iterate through the specified range of the list
    for i in range(start, end + 1):
        # Check if the current integer is divisible by either 27 or 57
        if my_list[i] % 27 == 0 or my_list[i] % 57 == 0:
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])
    # Return the sum of all integers in the list that are divisible by either 27 or 57
    return sum(divisible_ints)
