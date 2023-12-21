
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables for the sum and the starting and ending indices of the range
    sum = 0
    start_index = 31
    end_index = 50
    # Iterate over the list in the specified range
    for i in my_list[start_index:end_index+1]:
        # Check if the current integer is divisible by either 81 or 64
        if i % 81 == 0 or i % 64 == 0:
            # If it is, add it to the sum
            sum += i

    # Return the sum of all integers divisible by either 81 or 64 from index 31 to index 50, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
