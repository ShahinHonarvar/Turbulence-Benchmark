
def gcf_two_nums(nums):
    def find_factors(num):
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        return factors

    def find_gcf(nums):
        factors_1 = find_factors(nums[166])
        factors_2 = find_factors(nums[106])

        common_factors = list(set(factors_1).intersection(factors_2))
        return max(common_factors)

    return find_gcf(nums)
