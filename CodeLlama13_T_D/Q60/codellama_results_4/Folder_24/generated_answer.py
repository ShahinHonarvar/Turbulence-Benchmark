
def all_left_right_truncatable_prime(x):
    prime_numbers = []
    for i in range(2, x+1):
        if is_prime(i) and not contains_zero(str(i)):
            prime_numbers.append(i)

    left_truncatable_prime_numbers = []
    right_truncatable_prime_numbers = []
    for i in range(len(prime_numbers)):
        if is_left_truncatable_prime(str(prime_numbers[i])):
            left_truncatable_prime_numbers.append(prime_numbers[i])
        if is_right_truncatable_prime(str(prime_numbers[i])):
            right_truncatable_prime_numbers.append(prime_numbers[i])

    return sorted(left_truncatable_prime_numbers + right_truncatable_prime_numbers, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def contains_zero(s):
    return '0' in s

def is_left_truncatable_prime(s):
    for i in range(len(s)):
        if not is_prime(int(s[i:])):
            return False
    return True

def is_right_truncatable_prime(s):
    for i in range(len(s)-1, -1, -1):
        if not is_prime(int(s[:i+1])):
            return False
    return True
