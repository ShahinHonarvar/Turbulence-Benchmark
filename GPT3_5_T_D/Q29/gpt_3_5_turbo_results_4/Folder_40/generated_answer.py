
def gcf_two_nums(nums):
    def find_factors(num):
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        return factors
    
    num1 = nums[7]
    num2 = nums[9]
    factors1 = find_factors(num1)
    factors2 = find_factors(num2)
    common_factors = list(set(factors1) & set(factors2))
    common_factors.sort(reverse=True)
    return common_factors[0]
