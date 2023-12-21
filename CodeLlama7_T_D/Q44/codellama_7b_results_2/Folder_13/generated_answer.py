
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Loop through the list and check if each number is composite
    for i in range(21, 97 + 1):
        if is_composite(my_list[i]):
            composite_nums.add(my_list[i])

    return composite_nums

# Check if a number is composite by dividing it by all the numbers from 2 to sqrt(n)
def is_composite(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True

    return False
