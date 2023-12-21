
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[175]
    primes = []
    for i in range(2, x):
        num_str = str(i)
        valid = True
        while len(num_str) > 1:
            num_str = num_str[1:]
            if not is_prime(int(num_str)):
                valid = False
                break
        if valid:
            primes.append(i)
    return sorted(primes)
