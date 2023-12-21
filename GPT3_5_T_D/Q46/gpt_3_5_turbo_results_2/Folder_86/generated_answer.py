
def gcf_three_nums(nums):
    import math
    num1 = nums[341]
    num2 = nums[238]
    num3 = nums[374]
    return math.gcd(math.gcd(num1, num2), num3)
