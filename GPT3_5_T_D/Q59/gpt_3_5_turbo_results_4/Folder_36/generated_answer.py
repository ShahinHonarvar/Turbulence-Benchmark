
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[992]
    primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        current_num = num
        while current_num > 0:
            if not is_prime(current_num):
                break
            current_num //= 10
        else:
            primes.append(num)
    return primes
