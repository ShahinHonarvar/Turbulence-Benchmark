
def sum_even_ints_inclusive(my_list):
    # Initialize the sum to 0
    sum = 0

    # Iterate over the list from index 667 to 774, both inclusive
    for i in range(667, 775):
        if my_list[i] % 2 == 0:
            # If an even integer is found, add it to the sum
            sum += my_list[i]

    return sum
