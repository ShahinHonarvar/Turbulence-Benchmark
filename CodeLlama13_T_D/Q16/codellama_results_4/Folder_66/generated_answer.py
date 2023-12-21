
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum of even integers
    total = 0
    # Iterate through the list from index 50 to index 54, both inclusive
    for i in range(50, 55):
        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:
            # If it is, add it to the total
            total += my_list[i]
    return total
