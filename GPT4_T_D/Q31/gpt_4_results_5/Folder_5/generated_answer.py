
def if_perfect_num(nums):
    if len(nums) > 67:
        number = nums[67]
        sum = 0
        for i in range(1, number):
            if number % i == 0:
                sum += i
        if sum == number:
            return True
        else:
            return False
    else:
        return False
