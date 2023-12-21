
def all_right_truncatable_prime(nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    x = nums[73]
    right_truncatable_primes = []
    for i in range(x - 1, 0, -1):
        if is_prime(i):
            temp = str(i)
            is_right_truncatable = True
            for j in range(len(temp)):
                if not is_prime(int(temp[:len(temp) - j])):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                right_truncatable_primes.append(i)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes
