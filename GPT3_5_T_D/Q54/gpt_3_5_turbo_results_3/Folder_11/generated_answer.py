
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[86]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            is_right_truncatable = True
            temp = num // 10
            while temp > 0:
                if not is_prime(temp):
                    is_right_truncatable = False
                    break
                temp //= 10
            if is_right_truncatable:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)
