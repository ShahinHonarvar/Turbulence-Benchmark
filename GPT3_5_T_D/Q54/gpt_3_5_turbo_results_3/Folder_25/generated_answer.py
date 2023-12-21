
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_right_truncatable_primes_less_than(limit):
    primes = []
    for i in range(2, limit):
        if is_prime(i):
            num = str(i)
            truncatable = True
            for j in range(len(num)):
                if not is_prime(int(num[:j+1])):
                    truncatable = False
                    break
            if truncatable:
                primes.append(i)
    return primes

def all_right_truncatable_prime(numbers):
    x = numbers[92]
    primes = get_right_truncatable_primes_less_than(x)
    return sorted(primes)
