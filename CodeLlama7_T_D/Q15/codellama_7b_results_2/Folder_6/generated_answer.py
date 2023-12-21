
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list, starting from index 10
    for i in range(10, len(my_list)):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # Add the current element to the total sum
            total += my_list[i]

    # Return the sum of all odd integers from index 10 to index 66, both inclusive
    return total
