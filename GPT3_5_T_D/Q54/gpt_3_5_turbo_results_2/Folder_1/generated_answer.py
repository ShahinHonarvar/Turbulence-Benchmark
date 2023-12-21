
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[20]
    primes = []
    for i in range(x - 1, 1, -1):
        temp = str(i)
        while len(temp) > 0:
            if not is_prime(int(temp)):
                break
            temp = temp[:-1]
        else:
            primes.append(i)
    return sorted(primes, reverse=True)
