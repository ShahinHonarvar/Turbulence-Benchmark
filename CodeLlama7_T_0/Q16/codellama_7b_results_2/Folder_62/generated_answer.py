
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list from index 91 to index 99, both inclusive
    for i in range(91, 100):
        # If the current element is even, add it to the total
        if my_list[i] % 2 == 0:
            total += my_list[i]

    # Return the sum of all even integers from index 91 to index 99, both inclusive
    return total
