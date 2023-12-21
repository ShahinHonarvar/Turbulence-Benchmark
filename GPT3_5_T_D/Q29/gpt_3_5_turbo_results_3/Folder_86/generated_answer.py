
def gcf_two_nums(numbers):
    def find_factors(num):
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        return factors

    factors_793 = find_factors(numbers[793])
    factors_449 = find_factors(numbers[449])
    common_factors = list(set(factors_793) & set(factors_449))
    return max(common_factors)
