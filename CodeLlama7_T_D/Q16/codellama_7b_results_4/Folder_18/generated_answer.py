
def sum_even_ints_inclusive(my_list):
    # Initialize sum to 0
    sum = 0
    # Iterate through the list from index 35 to index 49, both inclusive
    for i in range(35, 50):
        # If the current element is even, add it to the sum
        if my_list[i] % 2 == 0:
            sum += my_list[i]
    return sum
