
def all_left_right_truncatable_prime(numbers):
    x = numbers[29]
    prime_numbers = []
    for i in range(10, x+1):
        if is_prime(i) and is_truncatable_prime(i):
            prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if len(str(n)) <= 1:
        return False
    for i in range(len(str(n))-1, 0, -1):
        if not is_prime(int(str(n)[:i])) or not is_prime(int(str(n)[i+1:])):
            return False
    return True
