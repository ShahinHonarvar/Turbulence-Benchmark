 def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    sum = 0
    # Iterate through the list from index 20 to index 30, both inclusive
    for i in range(20, 31):
        # If the current element is an odd integer, add it to the sum
        if my_list[i] % 2 != 0:
            sum += my_list[i]
    # Return the sum of all odd integers from index 20 to index 30, both inclusive. If no odd integers exist in the specified range, return 0.
    return sum
