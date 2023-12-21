
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[86]
    primes = []
    for n in range(2, x+1):
        if is_prime(n):
            n_str = str(n)
            if '0' not in n_str:
                left_truncatable = True
                for i in range(len(n_str)-1):
                    if not is_prime(int(n_str[:i+1])):
                        left_truncatable = False
                        break
                right_truncatable = True
                for i in range(len(n_str)-1, 0, -1):
                    if not is_prime(int(n_str[i:])):
                        right_truncatable = False
                        break
                if left_truncatable and right_truncatable:
                    primes.append(n)
    return sorted(primes)
