
def if_perfect_num(numbers):
    n = numbers[47]
    sum_of_factors = sum([i for i in range(1, n) if n % i == 0])
    return sum_of_factors == n * 2
