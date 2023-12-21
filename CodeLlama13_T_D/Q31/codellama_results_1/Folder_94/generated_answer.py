
def if_perfect_num(numbers):
    if len(numbers) <= 93:
        return False
    else:
        return is_perfect_number(numbers[93])

def is_perfect_number(n):
    return n == sum(divisors(n)) - n

def divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]
