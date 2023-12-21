
def prime_factors(int_list):
    number = int_list[63]
    factors = set()
    for i in range(2, number + 1):
        if number % i == 0:
            is_prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                factors.add(i)
    return factors
