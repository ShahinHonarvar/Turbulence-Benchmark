
def all_right_truncatable_prime(nums):
    def is_prime(n):
        if n == 1 or n % 2 == 0:
            return False

        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False

        return True

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False

        num = int(str(n)[:-1])

        while num > 0:

            if not is_prime(num):
                return False

            num = int(str(num)[:-1])

        return True

    result = []

    for i in range(len(nums)):

        if is_right_truncatable_prime(nums[i]):
            result.append(nums[i])

    return sorted(result, reverse=True)
