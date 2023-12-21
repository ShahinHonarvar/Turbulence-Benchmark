
def all_left_right_truncatable_prime(numbers):
    left_right_truncatable_primes = []
    for num in numbers:
        if str(num)[0] != '0':
            left_truncatable_prime = True
            right_truncatable_prime = True
            for i in range(1, len(str(num))):
                if not is_left_right_truncatable_prime(num, i):
                    left_truncatable_prime = False
                if not is_left_right_truncatable_prime(num, -i):
                    right_truncatable_prime = False
            if left_truncatable_prime and right_truncatable_prime:
                left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)

def is_left_right_truncatable_prime(num, i):
    if str(num)[i] == '0':
        return False
    else:
        return is_prime(int(str(num)[:i] + str(num)[-i:]))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
