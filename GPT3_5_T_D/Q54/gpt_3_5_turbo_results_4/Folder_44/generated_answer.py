
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[39]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            temp_num = num
            is_right_truncatable_prime = True
            while temp_num > 0:
                if not is_prime(temp_num):
                    is_right_truncatable_prime = False
                    break
                temp_num //= 10
            if is_right_truncatable_prime:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)
