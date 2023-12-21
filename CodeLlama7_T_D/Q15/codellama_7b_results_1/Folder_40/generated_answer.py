
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    sum = 0

    # Iterate through the list and find all odd integers
    for i in range(len(my_list)):
        if my_list[i] % 2 != 0:
            # Add the current integer to the sum
            sum += my_list[i]

    # Return the sum of all odd integers from index 0 to index 2, both inclusive
    return sum
