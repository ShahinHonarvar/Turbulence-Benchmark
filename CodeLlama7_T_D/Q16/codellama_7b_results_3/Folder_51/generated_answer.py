
def sum_even_ints_inclusive(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate over the list of integers, starting from index 1 and ending at index 8 (both inclusive)
    for i in range(1, 9):
        # If the current element is even, add it to the sum
        if my_list[i] % 2 == 0:
            sum += my_list[i]
    # Return the sum of all even integers from index 1 to index 8 (both inclusive)
    return sum
