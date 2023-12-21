
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list and add up the odd integers in the specified range
    for i in range(310, 370 + 1):
        if my_list[i] % 2 != 0:
            total += my_list[i]

    # Return the sum of all odd integers from index 310 to index 370, both inclusive. If no odd integers exist in the specified range, the function should return 0.
    return total
