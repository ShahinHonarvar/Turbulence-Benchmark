
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0
    # Iterate through the list and check if each element is even
    for i in range(75, 86):
        # If the current element is even, add it to the total
        if my_list[i] % 2 == 0:
            total += my_list[i]
    return total
