
def sum_odd_ints_inclusive(my_list):
    # Initialize the sum to 0
    sum = 0
    # Loop through the list of integers from index 50 to index 200, both inclusive
    for i in range(50, 201):
        # If the current element is an odd integer, add it to the sum
        if my_list[i] % 2 != 0:
            sum += my_list[i]
    # Return the sum of all odd integers from index 50 to index 200, both inclusive
    return sum
