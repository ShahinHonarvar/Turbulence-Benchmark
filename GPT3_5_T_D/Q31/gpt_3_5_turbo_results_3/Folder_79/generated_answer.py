
def if_perfect_num(nums):
    def is_perfect(num):
        divisors_sum = sum([i for i in range(1, int(num/2) + 1) if num % i == 0])
        return divisors_sum == num
    
    return is_perfect(nums[63])
