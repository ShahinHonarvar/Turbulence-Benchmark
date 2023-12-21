
def gcf_two_nums(numbers):
    def find_factors(num):
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        return factors

    factors1 = find_factors(numbers[25])
    factors2 = find_factors(numbers[80])

    common_factors = list(set(factors1) & set(factors2))

    return max(common_factors)
