
def sum_even_ints_inclusive(my_list):
    # Initialize sum to 0
    sum = 0
    # Loop through list from index 30 to index 87, both inclusive
    for i in range(30, 88):
        # If current element is even, add it to sum
        if my_list[i] % 2 == 0:
            sum += my_list[i]
    return sum
