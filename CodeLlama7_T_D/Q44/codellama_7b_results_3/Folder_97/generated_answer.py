
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Get the indices of the first and last composite numbers in the given list
    first_composite = next((i for i, x in enumerate(my_list) if is_composite(x)), None)
    last_composite = next((i for i, x in enumerate(reversed(my_list))) if is_composite(x)), None)
    # Get the set of all composite numbers between the first and last composite numbers in the given list
    return {my_list[i] for i in range(first_composite, last_composite + 1)}
# Check if a number is composite by dividing it by all prime numbers less than or equal to its square root
def is_composite(n):
    for p in range(2, int(n ** 0.5) + 1):
        if n % p == 0:
            return True

    return False
