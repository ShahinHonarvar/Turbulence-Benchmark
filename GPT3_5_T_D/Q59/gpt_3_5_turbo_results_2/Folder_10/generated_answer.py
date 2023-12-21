 
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[38]
    primes = []
    for num in range(x - 1, 2, -1):
        if '0' not in str(num):
            is_truncatable_prime = True
            n = num
            while n > 0:
                if not is_prime(n):
                    is_truncatable_prime = False
                    break
                n //= 10
            if is_truncatable_prime:
                primes.append(num)
    return sorted(primes, reverse=True)
