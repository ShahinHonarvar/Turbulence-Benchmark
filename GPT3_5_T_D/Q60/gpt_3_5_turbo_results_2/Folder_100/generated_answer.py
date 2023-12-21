
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for x in range(numbers[26] + 1):
        if is_prime(x):
            str_x = str(x)
            if '0' not in str_x:
                left_trunc = str_x
                right_trunc = str_x
                while len(left_trunc) > 1:
                    left_trunc = left_trunc[1:]
                    right_trunc = right_trunc[:-1]
                    if not is_prime(int(left_trunc)) or not is_prime(int(right_trunc)):
                        break
                else:
                    primes.append(x)
    return primes
