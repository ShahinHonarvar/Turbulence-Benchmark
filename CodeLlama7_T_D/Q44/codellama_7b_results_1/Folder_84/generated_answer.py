
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate through the list of positive integers
    for i in range(len(my_list)):
        # Check if the current number is between index 30 and 48, both inclusive
        if (i >= 30) and (i <= 48):
            # If the current number is composite, add it to the set of composite numbers
            if is_composite(my_list[i]):
                composite_nums.add(my_list[i])

    # Return the set of all composite numbers between index 30 and 48, both inclusive
    return composite_nums

# Function to check if a number is composite or not
def is_composite(n):
    # If the number is less than 2, it is not composite
    if n < 2:
        return False

    # Check if the number is divisible by any number between 2 and the square root of the number
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If the number is not divisible by any number between 2 and the square root of the number, it is composite
    return True
