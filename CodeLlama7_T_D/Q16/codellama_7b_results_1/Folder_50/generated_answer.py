
def sum_even_ints_inclusive(my_list):
    # Initialize the sum to 0
    total = 0
    # Iterate over the list from index 70 to index 84, both inclusive
    for i in range(70, 85):
        # If the current element is even, add it to the sum
        if my_list[i] % 2 == 0:
            total += my_list[i]
    return total
