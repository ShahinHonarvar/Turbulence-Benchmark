
def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        n = str(n)
        return all(is_prime(int(n[i:])) and is_prime(int(n[:-i or None])) for i in range(len(n)))

    x = nums[49]
    truncatables = [i for i in range(10, x+1) if '0' not in str(i) and is_truncatable(i)]
    truncatables.sort()
    return truncatables
