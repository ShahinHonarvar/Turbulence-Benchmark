
def all_right_truncatable_prime(nums):
    x = nums[10]

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable_prime(num):
        str_num = str(num)
        for i in range(len(str_num)):
            if not is_prime(int(str_num[i:])):
                return False
        return True

    right_truncatable_primes = [i for i in range(x) if is_right_truncatable_prime(i)]
    return sorted(right_truncatable_primes, reverse=True)
