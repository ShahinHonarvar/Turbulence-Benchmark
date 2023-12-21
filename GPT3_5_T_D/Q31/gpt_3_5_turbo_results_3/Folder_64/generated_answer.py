
def if_perfect_num(nums):
    def is_perfect(num):
        divisors = [x for x in range(1, num) if num % x == 0]
        return sum(divisors) == num
    
    return is_perfect(nums[1]) if len(nums) >= 2 else False
