
def all_right_truncatable_prime(nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    x = nums[6]
    right_truncatable_primes = []
    
    def check_right_truncatable_prime(num):
        if not is_prime(num):
            return False
        if len(str(num)) == 1:
            return True
        return check_right_truncatable_prime(int(str(num)[:-1]))

    for num in range(x-1, 0, -1):
        if check_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    
    return sorted(right_truncatable_primes, reverse=True)
