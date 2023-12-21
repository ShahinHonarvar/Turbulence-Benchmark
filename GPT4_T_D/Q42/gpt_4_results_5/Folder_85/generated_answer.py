
def prime_factors(numbers):
    number = numbers[23]
    factors = set()
    for i in range(2, number+1):
        if number % i == 0:
            is_prime = 1
            for j in range(2, (i//2+1)):
                if i % j == 0:
                    is_prime = 0
                    break
            if is_prime:
                factors.add(i)
    return factors
