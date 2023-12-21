
def prime_factors(numbers):
    integer_8 = numbers[8]
    factors = set()
    for i in range(2, integer_8 + 1):
        if integer_8 % i == 0:
            is_prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                factors.add(i)
    return factors
