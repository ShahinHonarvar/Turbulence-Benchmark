 def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0
    # Iterate through the list, starting from index 19 and ending at index 92 (both inclusive)
    for i in range(19, 93):
        # If the current element is even, add it to the sum
        if my_list[i] % 2 == 0:
            total += my_list[i]
    # Return the sum
    return total
