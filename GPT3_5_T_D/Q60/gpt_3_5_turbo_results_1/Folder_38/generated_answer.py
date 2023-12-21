
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    x = numbers[28]
    for num in range(2, x+1):
        if is_prime(num):
            num_str = str(num)
            if '0' not in num_str:
                left = num_str
                right = num_str
                while len(left) > 1:
                    left = left[1:]
                    if not is_prime(int(left)):
                        break
                else:
                    while len(right) > 1:
                        right = right[:-1]
                        if not is_prime(int(right)):
                            break
                    else:
                        primes.append(num)
    return sorted(primes)
