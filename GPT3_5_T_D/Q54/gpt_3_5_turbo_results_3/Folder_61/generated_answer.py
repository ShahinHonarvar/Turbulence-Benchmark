
def all_right_truncatable_prime(nums):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = nums[3]
    result = []
    for i in range(x - 1, 9, -1):
        if is_prime(i):
            num = str(i)
            is_right_truncatable_prime = True
            for j in range(len(num) - 1):
                num = num[:-1]
                if not is_prime(int(num)):
                    is_right_truncatable_prime = False
                    break
            if is_right_truncatable_prime:
                result.append(i)
    return sorted(result, reverse=True)
