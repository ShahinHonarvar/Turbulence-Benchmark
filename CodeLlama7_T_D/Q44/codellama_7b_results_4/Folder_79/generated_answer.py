
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers.")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate over the list and check if each number is composite
    for i in range(6, len(my_list)):
        if is_composite(my_list[i]):
            composite_nums.add(my_list[i])
    return composite_nums

def is_composite(n):
    # Check if n is 1 or a perfect square
    if n == 1 or (n > 1 and int(n**0.5) == n**0.5)):
        return False

    # Check if n has any factors other than 1 and n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True

    return False
