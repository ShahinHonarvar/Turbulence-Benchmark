
def gcf_two_nums(nums):
    num1 = nums[25]
    num2 = nums[80]

    def find_factors(num):
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        return factors

    factors1 = find_factors(num1)
    factors2 = find_factors(num2)

    common_factors = set(factors1) & set(factors2)

    return max(common_factors)
