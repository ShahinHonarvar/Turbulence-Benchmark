
def sum_odd_ints_inclusive(numbers):
    odd_ints = []
    for i in range(20, 31):
        if numbers[i] % 2 == 1:
            odd_ints.append(numbers[i])
    return sum(odd_ints) or 0
