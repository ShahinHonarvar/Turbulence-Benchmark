
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    sum = 0

    # Iterate through the list, starting from index 62 and ending at index 92
    for i in range(62, 93):
        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:
            # If it is, add it to the sum
            sum += my_list[i]

    # Return the sum
    return sum
