
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[88]
    primes = []
    for num in range(2, x + 1):
        if is_prime(num):
            truncatable = True
            for i in range(len(str(num))):
                left_truncated = int(str(num)[i:])
                right_truncated = int(str(num)[:len(str(num))-i])
                if left_truncated < 10 or right_truncated < 10:
                    continue
                if not is_prime(left_truncated) or not is_prime(right_truncated):
                    truncatable = False
                    break
            if truncatable:
                primes.append(num)
    primes.sort()
    return primes
