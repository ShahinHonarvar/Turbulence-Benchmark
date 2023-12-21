
def if_perfect_num(nums):
    def is_perfect(n):
        return n == sum(i for i in range(1, n//2 + 1) if n % i == 0)
    return is_perfect(nums[2])
