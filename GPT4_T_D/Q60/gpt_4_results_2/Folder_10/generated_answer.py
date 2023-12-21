
def all_left_right_truncatable_prime(nums):
    x = nums[38]
    
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def check_num(n):
        n = str(n)
        if '0' in n: return False
        for i in range(len(n)):
            if not is_prime(int(n[i:])) or not is_prime(int(n[:-i-1])):
                return False
        return True

    results = [i for i in range(11, x + 1) if check_num(i)]
    return sorted(results, reverse=True)
