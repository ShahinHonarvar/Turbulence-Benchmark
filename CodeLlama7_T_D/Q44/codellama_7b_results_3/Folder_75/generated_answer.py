
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Define the range of indices to check for composite numbers
    start_idx = 75
    end_idx = 85
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate over the input list and check if each element is a composite number in the specified range
    for i, num in enumerate(my_list):
        if start_idx <= i <= end_idx:
            if is_composite(num):
                composite_nums.add(num)
    # Return the set of all composite numbers in the specified range
    return composite_nums

def is_composite(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1)):
            # If i divides n with no remainder, return False
            if n % i == 0:
                return False

    # If n is a prime number, return True
    return True
