
def if_perfect_num(nums):
    def check_perfect_num(n):
        sum = 0
        for x in range(1, n):
            if n % x == 0:
                sum += x
        return sum == n

    if len(nums) > 85:
        return check_perfect_num(nums[85])
    else:
        return False
