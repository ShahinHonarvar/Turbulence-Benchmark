
def sum_even_ints_inclusive(my_list):
    # Initialize sum to 0
    sum = 0
    # Loop through list from index 60 to index 200, both inclusive
    for i in range(60, 201):
        # If current element is even, add it to sum
        if my_list[i] % 2 == 0:
            sum += my_list[i]
    return sum
