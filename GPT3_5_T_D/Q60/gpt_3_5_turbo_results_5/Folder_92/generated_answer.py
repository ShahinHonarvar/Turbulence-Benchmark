
def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_two_digit_prime(n):
        return n in [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        truncated = str(n)
        while len(truncated) > 1:
            truncated = truncated[1:-1]
            if not is_prime(int(truncated)):
                return False
        return True

    x = nums[7]
    results = []
    for num in range(2, x+1):
        if is_prime(num) and is_left_right_truncatable_prime(num):
            results.append(num)
    return sorted(results)
