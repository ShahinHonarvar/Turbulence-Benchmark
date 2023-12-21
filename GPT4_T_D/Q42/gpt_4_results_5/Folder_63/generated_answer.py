
def prime_factors(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        result = set()
        for i in range(2, n + 1):
            if n % i == 0 and is_prime(i):
                result.add(i)
        return result

    if len(numbers) > 57:
        return factors(numbers[57])
    else:
        return "The list has less than 58 elements"
