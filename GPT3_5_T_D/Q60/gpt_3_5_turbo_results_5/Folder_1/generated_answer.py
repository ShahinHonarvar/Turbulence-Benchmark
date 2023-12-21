
def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:i])):
                return False
        return True

    x = nums[20]
    result = []
    for num in range(2, x + 1):
        if is_prime(num) and is_truncatable_prime(num):
            result.append(num)
    result.sort(reverse=True)
    return result
