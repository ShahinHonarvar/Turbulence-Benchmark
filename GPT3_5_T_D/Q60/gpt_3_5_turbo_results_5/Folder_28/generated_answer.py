
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for x in numbers:
        if x < 11:
            continue
        for num in range(23, x+1):
            num_str = str(num)
            if '0' in num_str:
                continue
            for i in range(len(num_str)):
                left = int(num_str[:i+1])
                right = int(num_str[i:])
                if not is_prime(left) or not is_prime(right):
                    break
            else:
                primes.append(num)
    return sorted(primes)
