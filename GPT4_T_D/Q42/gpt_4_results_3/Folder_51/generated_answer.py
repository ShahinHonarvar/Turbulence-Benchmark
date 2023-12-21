
def prime_factors(numbers):
    num = numbers[64]
    factors = []
    for i in range(2, num):
        if num % i == 0:
            prime = True
            for j in range(2, (i // 2 + 1)):
                if i % j == 0:
                    prime = False
                    break
            if prime:
                factors.append(i)
    return set(factors)
