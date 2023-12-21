
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[31]
    right_truncatable_primes = []
    for num in range(x-1, 0, -1):
        if is_prime(num):
            current_num = str(num)
            is_right_truncatable = True
            while current_num:
                if not is_prime(int(current_num)):
                    is_right_truncatable = False
                    break
                current_num = current_num[:-1]
            if is_right_truncatable:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)
