
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[97]
    primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if is_prime(num):
            num_str = str(num)
            left_truncatable = True
            while len(num_str) > 1:
                num_str = num_str[1:]
                if not is_prime(int(num_str)):
                    left_truncatable = False
                    break
            if not left_truncatable:
                continue
            num_str = str(num)
            right_truncatable = True
            while len(num_str) > 1:
                num_str = num_str[:-1]
                if not is_prime(int(num_str)):
                    right_truncatable = False
                    break
            if right_truncatable:
                primes.append(num)
    return sorted(primes)
