
def all_right_truncatable_prime(numbers):
    def isPrime(n):
        if n < 2: return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def right_truncatable_prime(n):
        str_n = str(n)
        return all(isPrime(int(str_n[:i+1])) for i in range(len(str_n)))

    x = numbers[126]
    right_primes = [i for i in range(x) if right_truncatable_prime(i)]
    right_primes.sort(reverse=True)
    return right_primes
