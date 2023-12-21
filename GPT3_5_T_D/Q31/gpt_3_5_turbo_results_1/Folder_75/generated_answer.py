
def if_perfect_num(nums):
    def is_perfect_num(n):
        divisors = [x for x in range(1, n) if n % x == 0]
        return sum(divisors) == n

    num = nums[80] if len(nums) > 80 else None
    return is_perfect_num(num) if num else False
