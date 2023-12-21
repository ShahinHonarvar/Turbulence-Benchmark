
def all_right_truncatable_prime(numbers):
    x = numbers[69]
    prime_numbers = []
    for i in range(2, x+1):
        if is_prime(i):
            prime_numbers.append(i)
    right_truncatable_primes = []
    for i in prime_numbers:
        str_i = str(i)
        for j in range(len(str_i)):
            if is_right_truncatable_prime(str_i[:j]):
                right_truncatable_primes.append(int(str_i[:j]))
    return sorted(right_truncatable_primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(str_i):
    if not is_prime(int(str_i)):
        return False
    for j in range(len(str_i)-1, -1, -1):
        if not is_prime(int(str_i[:j])):
            return False
    return True
