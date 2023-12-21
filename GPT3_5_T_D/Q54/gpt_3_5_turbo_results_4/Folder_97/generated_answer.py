
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[645]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            num_str = str(num)
            all_truncatable = True
            for i in range(len(num_str)):
                truncated_num = int(num_str[:i+1])
                if not is_prime(truncated_num):
                    all_truncatable = False
                    break
            if all_truncatable:
                primes.append(num)
    return sorted(primes)
