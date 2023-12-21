
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    i = 80

    # Loop through the list from index 80 to 200, both inclusive
    while i <= 200:
        # Check if the current element is divisible by either 10 or 1000
        if my_list[i] % 10 == 0 or my_list[i] % 1000 == 0:
            # If it is, add it to the sum
            sum += my_list[i]

        # Increment the loop index
        i += 1

    # Return the sum of all integers divisible by either 10 or 1000 from index 80 to index 200, both inclusive
    return sum
