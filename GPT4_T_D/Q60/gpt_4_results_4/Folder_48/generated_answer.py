
def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_left_right_truncatable(n):
        n_str = str(n)
        if n_str.count('0') > 0:
            return False
        for i in range(len(n_str)):
            if not is_prime(int(n_str[i:])):
                return False
            if not is_prime(int(n_str[:len(n_str) - i])):
                return False
        return True

    x = nums[835]
    primes = []
    for num in range(x + 1):
        if is_left_right_truncatable(num):
            primes.append(num)

    return sorted(primes)
