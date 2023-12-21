
def gcf_two_nums(nums):
    def gcd(num1, num2):
        while num2 != 0:
            temp = num2
            num2 = num1 % num2
            num1 = temp
        return num1
    
    index1 = 33
    index2 = 72
    num1 = nums[index1]
    num2 = nums[index2]
    
    return gcd(num1, num2)
