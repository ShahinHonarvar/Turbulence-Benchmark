
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    sum = 0

    # Loop through the list and check if each element is an odd integer
    for i in range(55, 98 + 1):
        if my_list[i] % 2 != 0:
            # If the element is an odd integer, add it to the sum
            sum += my_list[i]

    # Return the sum of all odd integers from index 55 to index 98, both inclusive
    return sum
