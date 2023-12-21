
def all_right_truncatable_prime(nums):
    x = nums[758]

    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        string_num = str(n)
        for i in range(len(string_num)):
            if not is_prime(int(string_num[i:])):
                return False
        return True

    result = []

    for num in range(2, x):
        if is_right_truncatable(num):
            result.append(num)
    
    return sorted(result)
