
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[39]
    primes = []
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            temp = str(i)
            is_truncatable = True
            while temp != '':
                if not is_prime(int(temp)):
                    is_truncatable = False
                    break
                temp = temp[:len(temp) - 1]
            if is_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)
