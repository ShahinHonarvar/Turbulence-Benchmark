
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    sum = 0

    # Loop through the list, starting at index 59 and ending at index 97 (both inclusive)
    for i in range(59, 98):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the sum
            sum += my_list[i]

    # Return the sum
    return sum
