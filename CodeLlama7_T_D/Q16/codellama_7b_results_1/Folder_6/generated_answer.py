
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    sum = 0

    # Loop through the list, starting from index 10 and ending at index 66 (both inclusive)
    for i in range(10, 67):
        # If the current element is even, add it to the sum
        if my_list[i] % 2 == 0:
            sum += my_list[i]

    # Return the sum of all even integers from index 10 to index 66 (both inclusive), or 0 if no even integers exist in the specified range
    return sum
