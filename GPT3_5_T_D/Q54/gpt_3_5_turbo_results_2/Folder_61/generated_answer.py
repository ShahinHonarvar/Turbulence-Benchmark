
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[3]
    right_truncatable_primes = []
    for num in range(x-1, 1, -1):
        if is_prime(num):
            temp = num // 10
            while temp > 0:
                if not is_prime(temp):
                    break
                temp //= 10
            else:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)
