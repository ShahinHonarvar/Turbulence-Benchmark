
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    sum = 0

    # Loop through the list of integers
    for i in range(22, 89):
        # If the current index has an odd integer, add it to the sum
        if my_list[i] % 2 != 0:
            sum += my_list[i]

    # Return the sum of all odd integers from index 22 to index 88, both inclusive
    return sum
