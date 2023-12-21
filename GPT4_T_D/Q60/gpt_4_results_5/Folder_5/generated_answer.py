
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        if n == 2 or n == 3: 
            return True
        if n % 2 == 0 or n % 3 == 0: 
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True

    def is_truncatable(prime):
        str_prime = str(prime)
        if '0' in str_prime:
            return False
        for i in range(len(str_prime)):
            if not is_prime(int(str_prime[i:])) or not is_prime(int(str_prime[:len(str_prime) - i])):
                return False
        return True

    if not numbers or len(numbers) < 56:
        return []
    else:
        x = numbers[55]
        if x <= 2:
            return []

        truncatable_primes = []
        for i in range(10, x + 1):
            if is_prime(i) and is_truncatable(i):
                truncatable_primes.append(i)
        truncatable_primes.sort()
        return truncatable_primes
