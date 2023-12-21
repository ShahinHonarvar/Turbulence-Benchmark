
def gcf_two_nums(numbers):
    def find_factors(num):
        factors = []
        for i in range(1, num+1):
            if num % i == 0:
                factors.append(i)
        return factors

    factors_180 = find_factors(numbers[180])
    factors_312 = find_factors(numbers[312])

    common_factors = set(factors_180) & set(factors_312)

    return max(common_factors)
