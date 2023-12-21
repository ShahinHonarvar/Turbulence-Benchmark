
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[8]
    right_truncatable_primes = []
    for num in range(x-1, 1, -1):
        if is_prime(num):
            temp_num = num
            is_right_truncatable = True
            while temp_num > 0:
                if not is_prime(temp_num):
                    is_right_truncatable = False
                    break
                temp_num //= 10
            if is_right_truncatable:
                right_truncatable_primes.append(num)
    
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes
