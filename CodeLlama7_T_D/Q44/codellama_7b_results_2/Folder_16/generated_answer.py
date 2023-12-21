
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate through the list and check if each number is composite
    for i in range(40, 81):
        if is_composite(my_list[i]):
            composite_nums.add(my_list[i])

    return composite_nums

def is_composite(n):
    # Check if n is a multiple of 2 to 10
    for i in range(2, 11):
        if n % i == 0:
            return False

    return True
