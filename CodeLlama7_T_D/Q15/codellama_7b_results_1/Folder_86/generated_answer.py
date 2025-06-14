
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    sum = 0

    # Iterate through the list from index 31 to index 34, both inclusive
    for i in range(31, 35):

        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:

            # Add the current element to the sum
            sum += my_list[i]

    # Return the sum
    return sum
