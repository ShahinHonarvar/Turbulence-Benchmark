
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list, starting from index 40
    for i in range(40, len(my_list)):
        # Check if the current element is even
        if my_list[i] % 2 == 0:
            # If it is, add it to the total
            total += my_list[i]

    # Return the sum
    return total
