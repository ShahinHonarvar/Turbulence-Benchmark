
def sum_even_ints_inclusive(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate through the list, starting from index 30 and ending at index 48 (both inclusive)
    for i in range(30, 49):
        # If the current element is even, add it to the sum
        if my_list[i] % 2 == 0:
            sum += my_list[i]
    # Return the sum
    return sum
