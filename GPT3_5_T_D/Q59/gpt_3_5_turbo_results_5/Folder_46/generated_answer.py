
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[33]
    left_truncatable_primes = []
    for num in range(2, x):
        if "0" in str(num):
            continue
        temp = str(num)
        while temp:
            if not is_prime(int(temp)):
                break
            temp = temp[1:]
        else:
            left_truncatable_primes.append(num)
    return left_truncatable_primes
