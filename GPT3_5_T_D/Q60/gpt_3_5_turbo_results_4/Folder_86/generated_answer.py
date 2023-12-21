
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    x = numbers[126]
    for i in range(2, x + 1):
        if is_prime(i):
            num_str = str(i)
            if '0' not in num_str:
                is_truncatable = True
                for j in range(1, len(num_str)):
                    left = num_str[j:]
                    right = num_str[:-j]
                    if not is_prime(int(left)) or not is_prime(int(right)):
                        is_truncatable = False
                        break
                if is_truncatable:
                    primes.append(i)
    primes.sort(reverse=True)
    return primes
