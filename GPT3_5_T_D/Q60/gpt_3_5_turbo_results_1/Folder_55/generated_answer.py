
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[73]
    primes = []
    for num in range(2, x + 1):
        if is_prime(num):
            num_str = str(num)
            if '0' in num_str:
                continue
            for i in range(len(num_str)):
                if not is_prime(int(num_str[i:])):
                    break
                if not is_prime(int(num_str[:i+1])):
                    break
            else:
                primes.append(num)
    return sorted(primes, reverse=True)
