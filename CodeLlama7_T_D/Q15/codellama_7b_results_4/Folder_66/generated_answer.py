
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list and check if each element is an odd integer
    for i in range(50, 55):
        if my_list[i] % 2 != 0:
            # If the element is an odd integer, add it to the total
            total += my_list[i]

    # Return the sum of all odd integers from index 50 to index 54, both inclusive
    return total
