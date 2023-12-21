
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list and check if each element is a composite number
    for i in range(42, 68 + 1):
        if is_composite(my_list[i]):
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers between indices 42 and 68
    return composite_nums

# Check if a number is composite by dividing it by all prime numbers less than or equal to its square root
def is_composite(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True

    # If the number is not divisible by any prime number less than or equal to its square root, it is prime
    return False
