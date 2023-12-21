
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables for the start and end indices of the range of interest
    start = 34
    end = 81
    # Initialize a variable to store the sum
    sum = 0
    # Iterate through the range of interest
    for i in range(start, end + 1):
        # Check if the current integer is divisible by either 27 or 57
        if my_list[i] % 27 == 0 or my_list[i] % 57 == 0:
            # If it is, add it to the sum
            sum += my_list[i]
    # Return the sum of all integers divisible by either 27 or 57 from index 34 to index 81, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
