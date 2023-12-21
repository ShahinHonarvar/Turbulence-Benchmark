
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate through the list and check if each element is a composite number
    for i in range(222, len(my_list)):
        if is_composite(my_list[i]):
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers between indices 222 and 222, both inclusive
    return composite_nums

# Function to check if a number is composite or not
def is_composite(n):
    if n == 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True

    return False
