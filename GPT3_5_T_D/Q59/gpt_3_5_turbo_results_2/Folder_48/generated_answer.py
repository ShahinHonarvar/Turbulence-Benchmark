
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[835]
    truncatable_primes = []

    for num in range(2, x):
        if '0' not in str(num):
            is_truncatable_prime = True
            for i in range(1, len(str(num))):
                trunc_num = int(str(num)[i:])
                if not is_prime(trunc_num):
                    is_truncatable_prime = False
                    break
            if is_truncatable_prime:
                truncatable_primes.append(num)

    return sorted(truncatable_primes)
