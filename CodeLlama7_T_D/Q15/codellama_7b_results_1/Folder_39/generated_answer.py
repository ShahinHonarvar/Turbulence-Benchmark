
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list, starting from index 20 and ending at index 30 (both inclusive)
    for i in range(20, 31):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the sum
            total += my_list[i]

    # Return the sum of all odd integers in the specified range, or 0 if no such integers exist
    return total
