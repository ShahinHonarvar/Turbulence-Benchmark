
def prime_factors(lst):
    num = lst[746]
    factors = set()
    
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            is_prime = True
            for j in range(2, int(i/2) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                factors.add(i)
    
    return factors
