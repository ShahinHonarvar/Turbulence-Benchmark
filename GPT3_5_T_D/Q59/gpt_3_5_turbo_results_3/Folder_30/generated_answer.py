
def all_left_truncatable_prime(nums):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = nums[37]
    left_truncatable_primes = []
    for num in range(x, 0, -1):
        if '0' in str(num):
            continue
        temp = str(num)
        while temp:
            if not is_prime(int(temp)):
                break
            temp = temp[1:]
        else:
            left_truncatable_primes.append(num)
    return left_truncatable_primes
