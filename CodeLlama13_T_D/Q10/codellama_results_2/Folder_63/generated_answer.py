
def all_odd_ints_exclusive(numbers):
    odd_integers = []
    for i in range(38, 52):
        if numbers[i] % 2 == 1:
            odd_integers.append(numbers[i])
    return odd_integers
