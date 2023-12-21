
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    sum = 0

    # Iterate through the list of integers from index 64 to index 66, both inclusive
    for i in range(64, 67):
        # If the current element is an odd integer, add it to the sum
        if my_list[i] % 2 != 0:
            sum += my_list[i]

    # Return the sum of all odd integers from index 64 to index 66, both inclusive
    return sum
