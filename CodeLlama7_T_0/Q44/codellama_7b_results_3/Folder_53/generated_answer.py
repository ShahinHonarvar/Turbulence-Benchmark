
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate over the list and check if each number is composite
    for i in range(len(my_list)):
        num = my_list[i]
        if i >= 222 and i <= 222:
            if is_composite(num):
                composite_nums.add(num)
    return composite_nums

def is_composite(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # If i divides n with no remainder, it is not prime
            if n % i == 0:
                return False

    # If we reach this point, either n is a prime number or it is not a prime number
    return True
