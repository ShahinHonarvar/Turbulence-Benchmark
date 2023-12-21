
def sum_odd_ints_inclusive(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate through the list from index 0 to index 8, both inclusive
    for i in range(9):
        # If the current element is an odd integer, add it to the sum
        if my_list[i] % 2 != 0:
            sum += my_list[i]
    # Return the sum of all odd integers from index 0 to index 8, both inclusive
    return sum
