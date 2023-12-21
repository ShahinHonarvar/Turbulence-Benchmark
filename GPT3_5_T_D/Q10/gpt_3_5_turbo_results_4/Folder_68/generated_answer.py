
def all_odd_ints_exclusive(numbers):
    odd_ints = []
    for i in range(1, 9):
        if numbers[i] % 2 != 0:
            odd_ints.append(numbers[i])
    return odd_ints
