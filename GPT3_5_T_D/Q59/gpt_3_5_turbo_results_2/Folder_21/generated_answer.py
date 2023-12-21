
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[175]
    primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        truncatable = True
        temp = str(num)
        while temp:
            if not is_prime(int(temp)):
                truncatable = False
                break
            temp = temp[1:]
        if truncatable:
            primes.append(num)
    return primes
