
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Loop through the list and check if each number is composite
    for i in range(len(my_list)):
        num = my_list[i]
        if i >= 56 and i <= 57:
            if is_composite(num):
                composite_nums.add(num)

    # Return the set of all composite numbers between indices 56 to 57, inclusive
    return composite_nums

# Function to check if a number is composite
def is_composite(n):
    if n == 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True

    return False
