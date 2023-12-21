
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[65]
    right_truncatable_primes = []
    for num in range(x-1, 1, -1):
        if is_prime(num):
            is_right_truncatable = True
            num_str = str(num)
            while num_str:
                if not is_prime(int(num_str)):
                    is_right_truncatable = False
                    break
                num_str = num_str[:-1]
            if is_right_truncatable:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)
