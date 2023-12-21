
def all_right_truncatable_prime(nums):
    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for x in range(2, int(n**0.5) + 1):
            if n % x == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        n = str(n)
        for i in range(len(n)):
            if not is_prime(int(n[i:])):
                return False
        return True
    
    if len(nums)>69:
        x = nums[69]
    else:
        return []

    rtp_list = [i for i in range(2, x) if is_right_truncatable_prime(i)]

    return sorted(rtp_list, reverse=True)
