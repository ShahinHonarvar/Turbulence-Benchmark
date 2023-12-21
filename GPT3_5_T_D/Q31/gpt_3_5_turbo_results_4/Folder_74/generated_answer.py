
def if_perfect_num(nums):
    def is_perfect(num):
        divisor_sum = sum([i for i in range(1, num) if num % i == 0])
        return divisor_sum == num

    return is_perfect(nums[48])
