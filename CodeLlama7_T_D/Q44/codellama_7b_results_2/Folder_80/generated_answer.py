
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list and check if each number is composite
    for i in range(62, 78 + 1):
        if is_composite(my_list[i]):
            composite_nums.add(my_list[i])

    return composite_nums

# Check if a number is composite by dividing it by all the prime numbers less than or equal to its square root
def is_composite(n):
    # If the number is 1, it is not composite
    if n == 1:
        return False

    # If the number is greater than 1, it is composite if it is divisible by all prime factors less than or equal to its square root
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
