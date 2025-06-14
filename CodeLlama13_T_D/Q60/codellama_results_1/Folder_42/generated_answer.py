
def all_left_right_truncatable_prime(x):
    prime_numbers = []
    for i in range(2, x+1):
        if is_prime(i) and is_left_and_right_truncatable(i):
            prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_left_and_right_truncatable(n):
    if '0' in str(n):
        return False
    for i in range(len(str(n))-1, 0, -1):
        if not is_prime(int(str(n)[:i])):
            return False
    return True
