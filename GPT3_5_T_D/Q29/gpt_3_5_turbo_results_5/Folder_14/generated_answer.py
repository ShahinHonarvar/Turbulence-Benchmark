
def gcf_two_nums(nums):
    def find_factors(num):
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        return factors

    factors1 = find_factors(nums[49])
    factors2 = find_factors(nums[53])

    common_factors = [factor for factor in factors1 if factor in factors2]

    if not common_factors:
        return 1
    
    return max(common_factors)
