
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[8]
    primes = []
    for num in range(x-1, 1, -1):
        digits = list(str(num))
        if '0' not in digits:
            is_left_truncatable_prime = True
            for i in range(len(digits)-1):
                truncated_num = int(''.join(digits[i+1:]))
                if not is_prime(truncated_num):
                    is_left_truncatable_prime = False
                    break
            if is_left_truncatable_prime:
                primes.append(num)
    return sorted(primes, reverse=True)
