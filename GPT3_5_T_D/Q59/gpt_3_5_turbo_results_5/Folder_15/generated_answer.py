
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[6]
    truncatable_primes = []
    for num in range(x - 1, 1, -1):
        if '0' not in str(num):
            is_truncatable = True
            temp_num = num
            while temp_num > 0:
                if not is_prime(temp_num):
                    is_truncatable = False
                    break
                temp_num //= 10
            if is_truncatable:
                truncatable_primes.append(num)
    return truncatable_primes
