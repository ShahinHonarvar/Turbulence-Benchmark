
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    sum = 0

    # Loop through the list of integers from index 1 to index 1, both inclusive
    for i in range(1, len(my_list) + 1):

        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:

            # If it is, add it to the sum
            sum += my_list[i]

    # Return the sum of all odd integers from index 1 to index 1, both inclusive
    return sum
