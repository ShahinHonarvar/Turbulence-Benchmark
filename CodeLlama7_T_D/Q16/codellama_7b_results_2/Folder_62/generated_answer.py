
def sum_even_ints_inclusive(my_list):
    # Initialize the sum to 0
    total = 0

    # Iterate through the list, starting at index 91 and ending at index 99 (both inclusive)
    for i in range(91, 100):

        # If the current element is even, add it to the sum
        if my_list[i] % 2 == 0:
            total += my_list[i]

    # Return the sum

    return total
