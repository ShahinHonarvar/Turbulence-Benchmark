
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        length = len(str(n))
        for i in range(length):
            left = int(str(n)[i:])
            right = int(str(n)[:length-i])
            if not is_prime(left) or not is_prime(right):
                return False
        return True

    x = numbers[36]    
    truncatable_primes = [i for i in range(x + 1) if is_left_right_truncatable_prime(i)]
    return sorted(truncatable_primes, reverse=True)
