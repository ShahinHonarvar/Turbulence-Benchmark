
def all_left_truncatable_prime(nums):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        while num > 0:
            if not is_prime(num):
                return False
            num = int(str(num)[1:])
        return True

    x = nums[28]
    result = []
    for i in range(2, x):
        if str(i).find('0') == -1 and is_left_truncatable_prime(i):
            result.append(i)

    return sorted(result)
