
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    x = numbers[52]
    for num in range(2, x + 1):
        prime = True
        if '0' in str(num):
            continue
        truncated_num = num
        while truncated_num > 9:
            if not is_prime(truncated_num):
                prime = False
                break
            truncated_num //= 10
        if prime and is_prime(truncated_num):
            primes.append(num)
    
    return sorted(primes, reverse=True)
