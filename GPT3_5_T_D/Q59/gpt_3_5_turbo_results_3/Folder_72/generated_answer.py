
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[31]
    primes = []
    for i in range(2, x):
        if '0' in str(i):
            continue
        is_truncatable_prime = True
        temp = str(i)
        while temp != '':
            if not is_prime(int(temp)):
                is_truncatable_prime = False
                break
            temp = temp[1:]
        if is_truncatable_prime:
            primes.append(i)
    primes.sort(reverse=True)
    return primes
