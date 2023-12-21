
def if_perfect_num(nums):
    def is_perfect_number(num):
        if num <= 1:
            return False
        divisors_sum = 0
        for i in range(1, num):
            if num % i == 0:
                divisors_sum += i
        return divisors_sum == num
    
    if len(nums) >= 8 and is_perfect_number(nums[7]):
        return True
    else:
        return False
