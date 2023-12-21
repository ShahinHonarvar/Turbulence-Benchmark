
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[86]
    primes = []
    for num in range(2, x+1):
        if '0' not in str(num):
            prime = True
            for i in range(len(str(num))):
                if not is_prime(int(str(num)[i:])):
                    prime = False
                    break
                if not is_prime(int(str(num)[:i+1])):
                    prime = False
                    break
            if prime:
                primes.append(num)
    return sorted(primes, reverse=True)
