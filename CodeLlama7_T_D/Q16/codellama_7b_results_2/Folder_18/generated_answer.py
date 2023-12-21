
def sum_even_ints_inclusive(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate over the list, starting from index 35 and ending at index 49 (both inclusive)
    for i in range(35, 50):
        # Check if the current element is even
        if my_list[i] % 2 == 0:
            # If it is, add it to the sum
            sum += my_list[i]
    # Return the sum
    return sum
