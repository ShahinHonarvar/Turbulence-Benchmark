
def all_right_truncatable_prime(nums):
    x = nums[466]

    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable(num):
        for i in range(len(str(num))):
            if not is_prime(int(str(num)[i:])):
                return False
        return True

    result = []
    for num in range(2, x):
        if is_prime(num) and is_right_truncatable(num):
            result.append(num)

    return sorted(result, reverse=True)
