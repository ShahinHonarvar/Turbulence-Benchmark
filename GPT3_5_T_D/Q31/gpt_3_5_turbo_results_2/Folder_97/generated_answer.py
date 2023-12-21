
def if_perfect_num(nums):
    def is_perfect(num):
        if num <= 1:
            return False
        divisors_sum = 0
        for i in range(1, num):
            if num % i == 0:
                divisors_sum += i
        return divisors_sum == num
        
    if len(nums) > 132:
        return is_perfect(nums[132])
    else:
        return False
