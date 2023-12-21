
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    sum = 0

    # Loop through the list from index 10 to index 66, both inclusive
    for i in range(10, 67):

        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:

            # If it is an odd integer, add it to the sum
            sum += my_list[i]

    # Return the sum of all odd integers from index 10 to index 66, both inclusive
    return sum
