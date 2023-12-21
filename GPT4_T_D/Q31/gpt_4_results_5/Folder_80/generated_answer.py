
def if_perfect_num(nums):
    index = 746
    if index < len(nums):
        n = nums[index]
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors) == n
    else:
        return False
