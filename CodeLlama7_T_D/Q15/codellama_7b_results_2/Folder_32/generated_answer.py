
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list, starting from index 21
    for i in range(21, len(my_list)):
        # If the current element is odd, add it to the total
        if my_list[i] % 2 != 0:
            total += my_list[i]

    # Return the sum of all odd integers from index 21 to index 97, both inclusive
    return total
