
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[67]
    primes = []
    for num in range(2, x):
        if '0' not in str(num):
            is_truncatable = True
            temp = str(num)
            while temp:
                if not is_prime(int(temp)):
                    is_truncatable = False
                    break
                temp = temp[1:]
            if is_truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)
