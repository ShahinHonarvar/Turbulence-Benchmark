 def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0
    # Loop through the list, starting from index 4 (inclusive)
    for i in range(4, len(my_list)):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the total sum
            total += my_list[i]
    # Return the total sum
    return total
