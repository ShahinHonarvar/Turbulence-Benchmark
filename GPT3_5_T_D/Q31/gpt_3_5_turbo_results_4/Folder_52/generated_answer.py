
def if_perfect_num(nums):
    num = nums[478]
    factors = [1]
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            factors.append(i)
            if i != num//i:
                factors.append(num//i)
    if sum(factors) == num:
        return True
    return False
