
def prime_factors(numbers):
    num = numbers[0]
    factors = set()
    while num % 2 == 0:
        factors.add(2)
        num = num / 2
    i = 3
    while i * i <= num:
        if num % i == 0:
            factors.add(i)
            num = num / i
        else:
            i = i + 2
    if num > 2:
        factors.add(num)
    return factors
