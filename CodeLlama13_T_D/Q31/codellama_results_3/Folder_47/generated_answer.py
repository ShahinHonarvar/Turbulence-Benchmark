
def if_perfect_num(numbers):
    if len(numbers) <= 34:
        return False
    n = numbers[34]
    sum_divisors = sum(d for d in range(1, int(n**0.5) + 1) if n % d == 0)
    return sum_divisors == n
