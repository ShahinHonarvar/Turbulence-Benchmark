
def prime_factors(numbers):
    def prime(n):
        if n == 1:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True
    
    def factors(number):
        return set(filter(lambda x: number % x == 0, range(1, number+1)))

    number_63 = numbers[63]
    numbers_factors = factors(number_63)
    return set(filter(prime, numbers_factors))
