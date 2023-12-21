
def if_perfect_num(numbers):
    if len(numbers) <= 312:
        return False
    n = numbers[312]
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0 and (n // i) != i:
            return True
    return False
