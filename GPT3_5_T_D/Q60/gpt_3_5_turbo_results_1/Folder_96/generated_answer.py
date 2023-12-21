
def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        num_str = str(n)
        for i in range(len(num_str)):
            if num_str[i] == '0':
                return False
            if not is_prime(int(num_str[i:])):
                return False
            if not is_prime(int(num_str[:i+1])):
                return False
        return True

    x = nums[29]
    truncatable_primes = []
    for num in range(2, x+1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes
