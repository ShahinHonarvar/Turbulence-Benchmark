
def gcf_two_nums(numbers):
    def get_factors(num):
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        return factors

    factors_41 = get_factors(numbers[41])
    factors_69 = get_factors(numbers[69])

    common_factors = set(factors_41).intersection(factors_69)

    return max(common_factors)
