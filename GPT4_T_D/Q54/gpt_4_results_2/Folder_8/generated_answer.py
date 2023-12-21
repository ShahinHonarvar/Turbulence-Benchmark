
def all_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        str_num = str(n)
        while len(str_num) > 0:
            if not is_prime(int(str_num)):
                return False
            str_num = str_num[:-1]
        return True

    x = nums[41]
    prime_list = []
    for num in range(2, x):
        if is_prime(num) and is_right_truncatable(num):
            prime_list.append(num)

    return sorted(prime_list, reverse=True)
