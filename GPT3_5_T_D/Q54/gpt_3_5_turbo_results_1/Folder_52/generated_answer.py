
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[52]
    right_truncatable_primes = []
    for i in range(x - 1, 1, -1):
        num = str(i)
        flag = True
        while len(num) > 0:
            if not is_prime(int(num)):
                flag = False
                break
            num = num[:-1]
        if flag:
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)
