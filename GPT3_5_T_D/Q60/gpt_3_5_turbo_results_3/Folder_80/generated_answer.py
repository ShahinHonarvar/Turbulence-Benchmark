
def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_two_digit_prime(n):
        if n in [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
            return True
        return False
    
    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        if not is_prime(n):
            return False
        left_trunc = str(n)
        while len(left_trunc) > 1:
            left_trunc = left_trunc[1:]
            if not is_prime(int(left_trunc)):
                return False
        right_trunc = str(n)
        while len(right_trunc) > 1:
            right_trunc = right_trunc[:-1]
            if not is_prime(int(right_trunc)):
                return False
        return True
    
    x = nums[14]
    result = []
    for num in range(x, 0, -1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return result
