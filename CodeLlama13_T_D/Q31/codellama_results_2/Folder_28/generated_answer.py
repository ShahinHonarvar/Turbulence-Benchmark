
def if_perfect_num(numbers):
    if len(numbers) <= 37:
        return False
    n = numbers[37]
    sum_of_divisors = sum([d for d in range(1, int(n**0.5) + 1) if n % d == 0])
    return sum_of_divisors == n
