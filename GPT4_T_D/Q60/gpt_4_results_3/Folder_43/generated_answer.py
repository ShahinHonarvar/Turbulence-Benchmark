
def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n == 1: return False
        if n == 2: return True
        if n % 2 == 0: return False
        for i in range(3, int(n**0.5) + 1, 2):   
            if n % i == 0: return False
        return True

    def is_left_right_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:len(str_n)-i])):
                return False
        return True

    x = nums[89]
    result = []
    for i in range(2, x+1):
        if is_left_right_truncatable_prime(i):
            result.append(i)

    return sorted(result, reverse=True)
