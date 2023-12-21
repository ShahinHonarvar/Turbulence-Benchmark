
def all_left_right_truncatable_prime(x):
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and not contains_zero(str(i)):
            left_truncatable = True
            right_truncatable = True
            while len(str(i)) > 1:
                if not left_truncatable or not right_truncatable:
                    break
                i_str = str(i)
                left_truncatable = is_prime(int(i_str[1:]))
                right_truncatable = is_prime(int(i_str[:-1]))
            if left_truncatable and right_truncatable:
                primes.append(i)
    return sorted(primes)

def contains_zero(s):
    return '0' in s

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
