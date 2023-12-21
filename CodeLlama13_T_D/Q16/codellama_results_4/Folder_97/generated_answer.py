
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0
    # Iterate over the list and check if each element is even
    for i in range(40, 81):
        if my_list[i] % 2 == 0:
            # If an even integer is found, add it to the sum
            total += my_list[i]
    return total
