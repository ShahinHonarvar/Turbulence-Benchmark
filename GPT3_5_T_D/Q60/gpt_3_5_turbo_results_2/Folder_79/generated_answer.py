
def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        num_str = str(n)
        while num_str:
            if not is_prime(int(num_str)):
                return False
            num_str = num_str[1:-1]
        return True

    x = nums[91]
    primes = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            primes.append(num)

    return sorted(primes)
