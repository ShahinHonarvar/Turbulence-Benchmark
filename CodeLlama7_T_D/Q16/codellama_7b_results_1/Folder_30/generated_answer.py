
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    sum = 0

    # Iterate through the list, starting from index 55
    for i in range(55, len(my_list)):
        # If the current element is even, add it to the sum
        if my_list[i] % 2 == 0:
            sum += my_list[i]

    # Return the sum of all even integers from index 55 to index 98, both inclusive
    return sum
