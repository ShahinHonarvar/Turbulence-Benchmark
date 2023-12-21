
def prime_factors(lst):
    number = lst[746]
    factors = set()
    for i in range(2, number):
        while number % i == 0:
            factors.add(i)
            number /= i
        if number == 1:
            break
    if number!= 1:
        factors.add(number)
    return factors
