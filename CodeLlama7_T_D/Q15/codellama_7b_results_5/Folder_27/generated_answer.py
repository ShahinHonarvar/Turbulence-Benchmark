
def sum_odd_ints_inclusive(my_list):
    # Initialize variables to keep track of the sum and the current index
    sum = 0
    i = 66
    # Loop through the list, starting from index 66
    while i < len(my_list):
        # If the current element is an odd integer, add it to the sum
        if my_list[i] % 2 != 0:
            sum += my_list[i]
        # Increment the current index by 1
        i += 1
    # Return the sum of all odd integers from index 66 to index 93, inclusive
    return sum
