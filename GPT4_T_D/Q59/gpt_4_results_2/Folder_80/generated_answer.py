
def all_left_truncatable_prime(nums):
    x = nums[14]
    def is_prime(num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return False
            else:
                return True
        else:
            return False

    def left_truncatable(num):
        num_str = str(num)
        if '0' in num_str:
            return False
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])):
                return False
        return True

    truncatable_primes = []

    for num in range(2, x):
        if left_truncatable(num):
            truncatable_primes.append(num)

    return sorted(truncatable_primes, reverse=True)
