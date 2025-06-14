
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list of integers, starting from index 533 and ending at index 605 (inclusive)
    for i in range(533, 606):
        # If the current element is an odd integer, add it to the total sum
        if my_list[i] % 2 != 0:
            total += my_list[i]

    # Return the total sum of all odd integers in the specified range
    return total
