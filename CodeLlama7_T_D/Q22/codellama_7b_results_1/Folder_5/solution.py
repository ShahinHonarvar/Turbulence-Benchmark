def find_sum_of_multiples(n: int) -> int:
    return sum(i * n for i in range(1, 13 + 1))