
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[29]
    primes = []
    for i in range(2, x):
        num_str = str(i)
        is_left_truncatable = True
        while len(num_str) > 0:
            if num_str[0] == '0' or not is_prime(int(num_str)):
                is_left_truncatable = False
                break
            num_str = num_str[1:]

        if is_left_truncatable:
            primes.append(i)
    
    return sorted(primes, reverse=True)
