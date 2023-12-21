
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    primes = []
    for i in range(10, n):
        num = str(i)
        if '0' not in num:
            is_left_truncatable_prime = True
            for j in range(1, len(num)):
                if not is_prime(int(num[j:])):
                    is_left_truncatable_prime = False
                    break
            if is_left_truncatable_prime:
                primes.append(i)
    primes.sort(reverse=True)
    return primes

def all_left_truncatable_prime(numbers):
    x = numbers[73]
    return left_truncatable_prime(x)
