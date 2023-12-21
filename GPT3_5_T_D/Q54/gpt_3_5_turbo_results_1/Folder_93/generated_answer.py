
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[11]
    right_truncatable_primes = []
    for i in range(2, x):
        curr_num = i
        is_right_truncatable = True
        while curr_num > 0:
            if not is_prime(curr_num):
                is_right_truncatable = False
                break
            curr_num //= 10
        if is_right_truncatable:
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)
