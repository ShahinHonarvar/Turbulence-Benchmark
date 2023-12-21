
def sum_even_ints_inclusive(my_list):
    # Initialize the sum to 0
    total = 0
    # Loop through the list from index 40 to index 80, both inclusive
    for i in range(40, 81):
        # If the current element is even, add it to the sum
        if my_list[i] % 2 == 0:
            total += my_list[i]
    return total
