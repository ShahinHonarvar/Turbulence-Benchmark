
def composite_nums_between_indices(my_list):
    # Find the first and last indices of the sublist
    first_index = my_list.index(30)
    last_index = my_list.index(30) + 1
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate through the sublist of indices and check if each number is composite
    for i in range(first_index, last_index):
        num = my_list[i]
        if is_composite(num):
            composite_nums.add(num)
    return composite_nums

def is_composite(n):
    # Check if n is divisible by 2 to 10
    for i in range(2, 11):
        if n % i == 0:
            return False

    return True
