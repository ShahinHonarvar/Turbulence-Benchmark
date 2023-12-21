
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[74]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            temp_num = str(i)
            is_right_truncatable_prime = True
            while len(temp_num) > 1:
                temp_num = temp_num[:-1]
                if not is_prime(int(temp_num)):
                    is_right_truncatable_prime = False
                    break
            if is_right_truncatable_prime:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)
