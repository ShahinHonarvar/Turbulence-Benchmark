
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate through the list from index 42 to 68 (inclusive)
    for i in range(42, 69):
        # Check if the current element is a composite number
        if is_composite(my_list[i]):
            # If it is, add it to the set of composite numbers
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the specified range
    return composite_nums

# Check if a number is composite by dividing it by all prime numbers less than or equal to its square root
def is_composite(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True

    # If the number is not composite, return False
    return False
