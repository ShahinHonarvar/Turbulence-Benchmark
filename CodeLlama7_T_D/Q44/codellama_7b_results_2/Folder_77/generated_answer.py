 def composite_nums_between_indices(my_list):
    # Define a set to store the composite numbers
    composite_nums = set()
    # Loop through the list and check for composite numbers between indices 667 and 774, both inclusive
    for i in range(667, 774 + 1):
        # Check if the number is divisible by any number between 2 and the square root of the number
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                composite_nums.add(i)
    # Return the set of composite numbers found in the specified range
    return composite_nums
