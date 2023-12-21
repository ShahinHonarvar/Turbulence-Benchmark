
def all_right_truncatable_prime(nums):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = nums[70]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            str_num = str(num)
            is_right_truncatable = True
            for i in range(1, len(str_num)):
                truncated_num = int(str_num[:i])
                if not is_prime(truncated_num):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                primes.append(num)

    return sorted(primes)
