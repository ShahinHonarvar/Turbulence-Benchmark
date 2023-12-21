
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int( n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[41]
    right_truncatable_primes = []
    for i in range(x - 1, 0, -1):
        if is_prime(i):
            number = str(i)
            while number != '':
                if not is_prime(int(number)):
                    break
                number = number[:-1]
            else:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)
