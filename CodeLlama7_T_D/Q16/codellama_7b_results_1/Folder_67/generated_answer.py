
def sum_even_ints_inclusive(my_list):
    # Initialize sum to 0
    sum = 0
    # Iterate through list from index 22 to index 50, both inclusive
    for i in range(22, 51):
        # If current element is even, add it to sum
        if my_list[i] % 2 == 0:
            sum += my_list[i]
    return sum
