
def if_perfect_num(nums):
    for i in range(len(nums)):
        if nums[i] == 17:
            return is_perfect_number(nums[i])
    return False

def is_perfect_number(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n
