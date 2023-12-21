
def all_right_truncatable_prime(nums):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = nums[81]
    truncatable_primes = []

    for num in range(x-1, 1, -1):
        if is_prime(num):
            truncatable = True
            str_num = str(num)

            while truncatable and len(str_num) > 1:
                str_num = str_num[:-1]
                if not is_prime(int(str_num)):
                    truncatable = False

            if truncatable:
                truncatable_primes.append(num)

    truncatable_primes.sort(reverse=True)
    return truncatable_primes
