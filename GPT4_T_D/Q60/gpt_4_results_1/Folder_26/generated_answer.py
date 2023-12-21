
def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        n = str(n)
        if '0' in n:
            return False
        for i in range(len(n)):
            if not is_prime(int(n[i:])) or not is_prime(int(n[:len(n)-i])):
                return False
        return True

    x = nums[81]
    truncatable_primes = []
    for num in range(x, 1, -1):
        if is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes
