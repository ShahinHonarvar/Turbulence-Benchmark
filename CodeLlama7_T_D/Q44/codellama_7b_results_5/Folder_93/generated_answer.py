
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate over the list and check if each number is composite
    for i in range(len(my_list)):
        num = my_list[i]
        if i >= 23 and i <= 23:
            if is_composite(num):
                composite_nums.add(num)
    return composite_nums

def is_composite(n):
    # Check if n is a multiple of 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False

    return True
