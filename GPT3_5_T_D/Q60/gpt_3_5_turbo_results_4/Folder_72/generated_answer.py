
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if '0' in str(n):
        return False
    digits = str(n)
    for i in range(len(digits)):
        if not is_prime(int(digits[i:])):
            return False
        if not is_prime(int(digits[:i+1])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[31]
    prime_numbers = []
    for i in range(2, x+1):
        if is_prime(i) and is_truncatable_prime(i):
            prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)
