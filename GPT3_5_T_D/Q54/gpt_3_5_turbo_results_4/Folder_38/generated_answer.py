
def all_right_truncatable_prime(nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    x = nums[28]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            is_right_truncatable_prime = True
            temp = str(num)
            while len(temp) > 1:
                temp = temp[:-1]
                if is_prime(int(temp)) is False:
                    is_right_truncatable_prime = False
                    break
            if is_right_truncatable_prime:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)
