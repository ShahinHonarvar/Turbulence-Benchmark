
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables to keep track of the sum and the index
    total = 0
    i = 0
    # Loop through the list of integers
    while i < len(my_list):
        # If the current integer is divisible by either 10 or 100, add it to the total
        if my_list[i] % 10 == 0 or my_list[i] % 100 == 0:
            total += my_list[i]
        # Increment the index by 1 for the next iteration of the loop
        i += 1
    # Return the sum of all integers divisible by either 10 or 100 from index 0 to index 9, both inclusive
    return total
