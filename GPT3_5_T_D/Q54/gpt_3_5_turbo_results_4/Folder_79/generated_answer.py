
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    if len(numbers) < 92:
        return []
    x = numbers[91]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            is_truncatable_prime = True
            num_str = str(num)
            while len(num_str) > 1:
                num_str = num_str[:-1]
                if not is_prime(int(num_str)):
                    is_truncatable_prime = False
                    break
            if is_truncatable_prime:
                primes.append(num)
    return sorted(primes)
