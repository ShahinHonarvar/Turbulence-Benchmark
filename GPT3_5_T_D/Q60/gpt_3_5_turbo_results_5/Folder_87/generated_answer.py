
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if is_prime(num) and '0' not in str(num):
            left_truncatable = True
            right_truncatable = True
            for i in range(len(str(num))-1):
                left_trunc = int(str(num)[i+1:])
                right_trunc = int(str(num)[:-i-1])
                if not is_prime(left_trunc):
                    left_truncatable = False
                if not is_prime(right_trunc):
                    right_truncatable = False
            if left_truncatable and right_truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)
