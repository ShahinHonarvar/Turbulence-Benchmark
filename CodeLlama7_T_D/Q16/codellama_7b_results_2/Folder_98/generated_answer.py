
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list and check if each integer is even
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            # If the integer is even, add it to the sum
            total += my_list[i]

    # Return the sum of all even integers from index 0 to index 6, both inclusive
    return total
