
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[30]
    right_trunc_primes = []
    for num in range(2, x):
        if is_prime(num):
            temp_num = num
            is_trunc_prime = True
            while temp_num > 10:
                temp_num //= 10
                if not is_prime(temp_num):
                    is_trunc_prime = False
                    break
            if is_trunc_prime:
                right_trunc_primes.append(num)
    return sorted(right_trunc_primes)
