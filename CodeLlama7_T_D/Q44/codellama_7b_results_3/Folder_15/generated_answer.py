
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Define a set to store the composite numbers
    composite_nums = set()
    # Iterate through the list and check if each number is composite
    for i in range(len(my_list)):
        num = my_list[i]
        if is_composite(num):
            composite_nums.add(num)
    return composite_nums

def is_composite(n):
    # Check if n is a multiple of 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return True
    # Check if n is a multiple of 4, 5, or 6
    for i in range(4, int(n ** 0.5) + 1, 4):
        if n % i == 0:
            return True

    return False
