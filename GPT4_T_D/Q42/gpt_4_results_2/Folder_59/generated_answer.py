
def prime_factors(lst):
    number = lst[2]
    factors = set()
    i = 2
    while number > 1:
        if number % i == 0:
            factors.add(i)
            number = number//i
            i = i-1
        i = i+1
    return factors
