
def prime_factors(lst):
    number = lst[93]
    factors = set()
    while number % 2 == 0:
        factors.add(2)
        number = number // 2
    for i in range(3, int(number ** 0.5) + 1, 2):
        while number % i == 0:
            factors.add(i)
            number = number // i
    if number > 2:
        factors.add(number)
    return factors
