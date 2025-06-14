
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list of integers, starting from index 0
    for i in range(len(my_list)):
        # If the current element is even, add it to the total
        if my_list[i] % 2 == 0:
            total += my_list[i]

    # Return the sum of all even integers from index 0 to index 2, both inclusive
    return total
