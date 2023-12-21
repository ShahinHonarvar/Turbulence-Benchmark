
def sum_even_ints_inclusive(my_list):
    # Initialize the sum to 0
    total = 0
    # Loop through the list of integers, starting from index 0
    for i in range(len(my_list)):
        # If the current element is even, add it to the sum
        if my_list[i] % 2 == 0:
            total += my_list[i]
    return total
