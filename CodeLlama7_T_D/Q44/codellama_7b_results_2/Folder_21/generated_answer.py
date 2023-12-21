
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate through the list and check if each element is composite
    for i in range(262, 747):
        if is_composite(my_list[i]):
            composite_nums.add(my_list[i])
    return composite_nums

# Check if a number is composite by dividing it by all the prime numbers less than or equal to its square root
def is_composite(n):
    for i in range(int(n ** 0.5), 1, -1):
        if n % i == 0:
            return True

    return False
