
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for x in numbers:
        if x < 10:
            continue
        if is_prime(x):
            str_x = str(x)
            if '0' in str_x:
                continue
            is_left_truncatable_prime = True
            is_right_truncatable_prime = True
            for i in range(len(str_x)):
                if not is_prime(int(str_x[i:])):
                    is_right_truncatable_prime = False
                    break
                if not is_prime(int(str_x[:len(str_x)-i])):
                    is_left_truncatable_prime = False
                    break
            if is_left_truncatable_prime and is_right_truncatable_prime:
                primes.append(x)
    return sorted(primes, reverse=True)
