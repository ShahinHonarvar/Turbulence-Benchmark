
def if_perfect_num(nums):
    num_at_index_17 = nums[17]
    divisors = [i for i in range(1, num_at_index_17) if num_at_index_17 % i == 0]
    if sum(divisors) == num_at_index_17:
        return True
    else:
        return False
