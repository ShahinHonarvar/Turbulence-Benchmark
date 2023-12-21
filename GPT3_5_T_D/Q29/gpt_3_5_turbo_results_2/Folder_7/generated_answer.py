
def gcf_two_nums(nums):
    def find_factors(n):
        factors = set()
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                factors.add(i)
                factors.add(n // i)
        return factors

    factors_224 = find_factors(nums[224])
    factors_663 = find_factors(nums[663])

    common_factors = factors_224.intersection(factors_663)
    greatest_common_factor = max(common_factors)

    return greatest_common_factor
