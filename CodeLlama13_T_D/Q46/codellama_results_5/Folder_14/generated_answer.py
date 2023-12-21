
def gcf_three_nums(numbers):
    return max([x for x in range(1, numbers[0]) if all([numbers[i] % x == 0 for i in (17, 88, 35)])])
