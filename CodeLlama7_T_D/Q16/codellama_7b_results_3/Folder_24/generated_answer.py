
def sum_even_ints_inclusive(my_list):
    # Initialize the sum to 0
    total = 0
    # Loop through the list, starting from index 74
    for i in range(74, len(my_list)):
        # If the current element is even, add it to the sum
        if my_list[i] % 2 == 0:
            total += my_list[i]
    return total
