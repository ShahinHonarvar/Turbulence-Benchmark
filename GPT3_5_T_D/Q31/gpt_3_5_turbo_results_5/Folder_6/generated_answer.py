
def if_perfect_num(nums):
    def is_perfect_num(n):
        divisors = []
        for i in range(1, n):
            if n % i == 0:
                divisors.append(i)
        return sum(divisors) == n
    
    if len(nums) > 790:
        return is_perfect_num(nums[790])
    return False
