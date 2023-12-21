
def if_perfect_num(numbers):
    return numbers[80] in perfect_numbers(numbers)

def perfect_numbers(numbers):
    return [n for n in numbers if is_perfect_number(n)]

def is_perfect_number(n):
    return n == sum(divisors(n))

def divisors(n):
    return [i for i in range(1, int(n ** 0.5) + 1) if n % i == 0]
