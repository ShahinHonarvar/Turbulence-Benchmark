
def if_perfect_num(nums):
    def is_perfect(num):
        divisors_sum = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors_sum += i
                if i != num // i:
                    divisors_sum += num // i
        return divisors_sum == num
    
    if len(nums) > 84:
        return is_perfect(nums[84])
    else:
        return False
