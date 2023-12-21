
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for number in numbers:
        if number <= 10:
            continue
        num_str = str(number)
        if '0' in num_str:
            continue
        is_truncatable_prime = True
        for i in range(1, len(num_str)):
            left_truncated = int(num_str[i:])
            right_truncated = int(num_str[:-i])
            if not is_prime(left_truncated) or not is_prime(right_truncated):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            primes.append(number)
    primes.sort(reverse=True)
    return primes
