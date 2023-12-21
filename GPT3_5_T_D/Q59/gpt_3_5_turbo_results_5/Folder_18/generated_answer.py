
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            num = str(i)
            is_truncatable = True
            for j in range(len(num)):
                trunc_num = int(num[j:])
                if not is_prime(trunc_num):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)

def all_left_truncatable_prime(numbers):
    x = numbers[429]
    return left_truncatable_prime(x)
