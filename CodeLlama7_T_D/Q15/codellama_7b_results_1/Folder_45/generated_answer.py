
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list, starting from index 30 and ending at index 200 (both inclusive)
    for i in range(30, 201):

        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:

            # If it is, add it to the sum
            total += my_list[i]

    # Return the sum
    return total
