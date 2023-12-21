
def prime_factors(numbers):
    num = numbers[19]

    factors = []
    for i in range(2, num+1):
        if num % i == 0:
            is_prime = 1
            for j in range(2, (i //2 + 1)):
                if i % j == 0:
                    is_prime = 0
                    break
            
            if is_prime == 1:
                factors.append(i)

    return set(factors)
