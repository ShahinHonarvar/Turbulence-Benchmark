
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list and find all odd integers in the specified range
    for i in range(40, 81):
        if my_list[i] % 2 != 0:
            total += my_list[i]

    # Return the sum of all odd integers in the specified range, or 0 if no such integers exist
    return total
