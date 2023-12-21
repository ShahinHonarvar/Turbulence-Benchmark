
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[32]
    truncatable_primes = []
    for num in range(2, x+1):
        str_num = str(num)
        if '0' in str_num:
            continue
        is_truncatable = True
        for i in range(len(str_num)):
            truncated_num = int(str_num[i:])
            if not is_prime(truncated_num):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(num)
    return truncatable_primes
