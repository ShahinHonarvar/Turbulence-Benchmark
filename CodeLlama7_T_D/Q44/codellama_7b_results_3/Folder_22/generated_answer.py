
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list and check if each number is composite
    for i in range(50, 201):
        if is_composite(my_list[i]):
            composite_nums.add(my_list[i])

    return composite_nums

def is_composite(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # If n is divisible by any number between 2 and the square root of n, it is not prime
            if n % i == 0:
                return False

    return True
