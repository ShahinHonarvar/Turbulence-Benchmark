
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list, starting from index 30 and ending at index 87 (both inclusive)
    for i in range(30, 87 + 1):

        # If the current element is an odd integer, add it to the sum
        if my_list[i] % 2 != 0:
            total += my_list[i]

    # Return the sum of all odd integers from index 30 to index 87 (both inclusive), or 0 if no such integers exist.
    return total
