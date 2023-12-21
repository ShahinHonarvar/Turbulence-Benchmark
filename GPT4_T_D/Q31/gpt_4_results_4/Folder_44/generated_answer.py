
def if_perfect_num(nums):
    if len(nums) <= 828:
        return False
    
    number = nums[828]
    factors = [i for i in range(1,number) if number%i==0]
    return sum(factors) == number
