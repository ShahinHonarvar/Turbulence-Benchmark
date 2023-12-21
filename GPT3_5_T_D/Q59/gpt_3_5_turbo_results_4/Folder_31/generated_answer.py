
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[50]
    left_truncatable_primes = []
    for i in range(2, x):
        num = str(i)
        is_truncatable_prime = True
        if '0' in num:
            is_truncatable_prime = False
        else:
            for j in range(len(num)):
                truncated_num = int(num[j:])
                if not is_prime(truncated_num):
                    is_truncatable_prime = False
                    break
        if is_truncatable_prime:
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)
