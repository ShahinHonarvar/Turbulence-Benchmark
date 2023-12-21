
def prime_factors(numbers):
    def prime_check(num):
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True

    def factors(num):
        factors_list = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors_list.append(i)
        return factors_list

    number = numbers[88]
    all_factors = factors(number)
    primes = {x for x in all_factors if prime_check(x)}

    return primes
