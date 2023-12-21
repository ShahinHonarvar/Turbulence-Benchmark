
def gcf_two_nums(nums):
    def find_factors(num):
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        return factors

    factors_85 = find_factors(nums[85])
    factors_51 = find_factors(nums[51])

    common_factors = set(factors_85).intersection(factors_51)

    return max(common_factors)
