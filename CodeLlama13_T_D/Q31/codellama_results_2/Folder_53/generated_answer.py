
def if_perfect_num(numbers):
    return numbers[73] in perfect_nums(numbers)

def perfect_nums(numbers):
    return [n for n in numbers if is_perfect_num(n)]

def is_perfect_num(n):
    return sum(divisors(n)) == 2 * n

def divisors(n):
    return [d for d in range(1, int(n ** 0.5) + 1) if n % d == 0]
