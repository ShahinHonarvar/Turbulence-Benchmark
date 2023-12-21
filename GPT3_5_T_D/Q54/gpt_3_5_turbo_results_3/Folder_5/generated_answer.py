
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[55]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            is_right_truncatable_prime = True
            current_num = num
            while current_num > 0:
                if not is_prime(current_num):
                    is_right_truncatable_prime = False
                    break
                current_num //= 10
            if is_right_truncatable_prime:
               right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)
