 def sum_odd_ints_inclusive(my_list):
    # Initialize sum to 0
    sum = 0
    # Iterate through list from index 75 to index 85, both inclusive
    for i in range(75, 86):
        # If current element is an odd integer, add it to sum
        if my_list[i] % 2 != 0:
            sum += my_list[i]
    return sum
