
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Loop through the list of positive integers
    for i in range(len(my_list)):
        # Check if the current number is between index 667 and index 774, both inclusive
        if 667 <= i <= 774:
            # If the current number is composite, add it to the set of composite numbers
            if is_composite(my_list[i]):
                composite_nums.add(my_list[i])
    return composite_nums

# Define a function to check if a number is composite
def is_composite(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop through the numbers from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # If any of the numbers between 2 and the square root of n divides n without leaving a remainder, return False
            if n % i == 0:
                return False

    # If no numbers from 2 to the square root of n divide n without leaving a remainder, return True
    return True
