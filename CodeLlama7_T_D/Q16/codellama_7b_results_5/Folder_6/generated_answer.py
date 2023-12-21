
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list, starting from index 10
    for i in range(10, len(my_list)):
        # If the current element is even, add it to the total
        if my_list[i] % 2 == 0:
            total += my_list[i]

    # Return the sum of all even integers from index 10 to index 66, both inclusive
    return total
