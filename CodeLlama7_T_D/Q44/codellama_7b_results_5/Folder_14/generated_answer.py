
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate through the list and check if each number is composite
    for i in range(4, len(my_list)):
        if is_composite(my_list[i]):
            # If the number is composite, add it to the set
            composite_nums.add(my_list[i])

    return composite_nums

# Check if a number is composite by dividing it by all numbers less than or equal to its square root
def is_composite(n):
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            return True

    return False
