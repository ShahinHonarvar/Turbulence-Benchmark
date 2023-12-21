
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[69]
    primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        prime = True
        for i in range(len(str(num))):
            truncated_num = int(str(num)[i:])
            if not is_prime(truncated_num):
                prime = False
                break
        if prime:
            primes.append(num)
    return sorted(primes, reverse=True)
