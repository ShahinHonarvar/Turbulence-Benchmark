
def composite_nums_between_indices(my_list):
    # Define a set to store the composite numbers
    composite_nums = set()

    # Iterate through the list and check if each number is composite
    for i in range(62, 100):
        if is_composite(my_list[i]):
            composite_nums.add(my_list[i])

    # Return the set of composite numbers between indices 62 to 99
    return composite_nums

# Define a function to check if a number is composite
def is_composite(n):
    if n == 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True

    return False
