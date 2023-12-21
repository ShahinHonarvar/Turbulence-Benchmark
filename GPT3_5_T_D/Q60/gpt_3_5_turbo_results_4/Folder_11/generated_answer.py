 

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def truncate_left(n):
    s = str(n)
    return int(s[1:])

def truncate_right(n):
    s = str(n)
    return int(s[:-1])

def all_left_right_truncatable_prime(numbers):
    x = numbers[86]
    primes = []
    for i in range(2, x+1):
        if is_prime(i):
            left_truncated = i
            right_truncated = i
            while len(str(left_truncated)) > 1:
                left_truncated = truncate_left(left_truncated)
                if not is_prime(left_truncated):
                    break
            while len(str(right_truncated)) > 1:
                right_truncated = truncate_right(right_truncated)
                if not is_prime(right_truncated):
                    break
            if len(str(left_truncated)) <= 2 and len(str(right_truncated)) <= 2:
                primes.append(i)
    return sorted(primes)
