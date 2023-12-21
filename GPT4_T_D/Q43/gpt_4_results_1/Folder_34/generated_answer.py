
def find_primes_between_indices(numbers):
    from sympy import isprime

    result = [num for num in numbers[56:58] if isprime(num)]
    result.sort(reverse=True)

    return result
