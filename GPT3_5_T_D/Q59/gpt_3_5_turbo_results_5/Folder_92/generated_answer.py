
def is_prime(n):
    if n in (2, 3):
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[7]
    truncatable_primes = []
    for num in range(2, x):
        if '0' not in str(num):
            num_str = str(num)
            truncatable_prime = True
            for i in range(len(num_str)):
                if not is_prime(int(num_str[i:])):
                    truncatable_prime = False
                    break
            if truncatable_prime:
                truncatable_primes.append(num)
    return truncatable_primes
