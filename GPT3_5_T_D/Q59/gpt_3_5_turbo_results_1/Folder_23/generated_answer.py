
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[77]
    primes = []
    for num in range(x-1, 0, -1):
        if '0' in str(num):
            continue
        is_left_truncatable_prime = True
        for i in range(len(str(num))):
            truncated_num = int(str(num)[i:])
            if not is_prime(truncated_num):
                is_left_truncatable_prime = False
                break
        if is_left_truncatable_prime:
            primes.append(num)
    return primes
