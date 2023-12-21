
def all_left_right_truncatable_prime(numbers):
    import sympy
    def is_truncatable_prime(num):
        num = str(num)
        if "0" in num: 
            return False
        for i in range(len(num)):
            if not sympy.isprime(int(num[i:])) or not sympy.isprime(int(num[:len(num)-i])):
                return False
        return True

    x = numbers[370]
    truncatable_primes = []
    for num in range(11, x+1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
