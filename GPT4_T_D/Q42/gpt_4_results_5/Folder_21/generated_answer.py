
def prime_factors(numbers):
    number = numbers[410]
    factors = set()
    for i in range(2, int(number**0.5)+1):
        while (number % i==0):
            factors.add(i)
            number = number // i
    if number > 2:
        factors.add(number)
    return factors
