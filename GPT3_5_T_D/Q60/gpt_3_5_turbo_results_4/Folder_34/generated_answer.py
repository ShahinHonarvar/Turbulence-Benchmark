
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
            left_right_truncatable = True
            for i in range(len(str(num))):
                left_truncation = int(str(num)[i:])
                right_truncation = int(str(num)[:len(str(num))-i])
                if (len(str(left_truncation)) > 2 or len(str(right_truncation)) > 2) and not is_prime(left_truncation) and not is_prime(right_truncation):
                    left_right_truncatable = False
                    break
            if left_right_truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)
