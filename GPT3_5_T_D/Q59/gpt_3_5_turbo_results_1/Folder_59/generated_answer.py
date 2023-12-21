
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[84]
    primes = []
    for i in range(2, x):
        if i == 2 or i == 3 or i == 5 or i == 7:
            primes.append(i)
            continue
        string = str(i)
        if '0' in string:
            continue
        is_truncatable_prime = True
        for j in range(len(string)-1):
            if not is_prime(int(string[j+1:])):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            primes.append(i)
    primes.sort(reverse=True)
    return primes
