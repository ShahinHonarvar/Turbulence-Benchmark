
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    sum = 0
    # Iterate through the list, starting from index 62 and ending at index 99 (both inclusive)
    for i in range(62, 100):
        # If the current element is even, add it to the sum
        if my_list[i] % 2 == 0:
            sum += my_list[i]
    # Return the sum
    return sum
