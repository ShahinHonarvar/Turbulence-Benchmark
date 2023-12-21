
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[55]
    primes = []
    for i in range(1, x):
        num = str(i)
        prime = True
        while num != "":
            if not is_prime(int(num)):
                prime = False
                break
            num = num[1:]
        if prime:
            primes.append(i)
    return sorted(primes, reverse=True)
