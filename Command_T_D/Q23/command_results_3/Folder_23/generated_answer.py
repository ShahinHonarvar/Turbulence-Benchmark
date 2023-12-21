def find_divisors_in_range(n):
    d = list(range(18, n + 1, n))
    return [i for i in d if all(i % j == 0 for j in range(2, i // 2 + 1))]
