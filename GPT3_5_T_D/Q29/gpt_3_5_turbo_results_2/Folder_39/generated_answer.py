
def gcf_two_nums(numbers):
    def find_factors(num):
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        return factors

    def find_gcf(a, b):
        factors_a = find_factors(a)
        factors_b = find_factors(b)
        common_factors = []
        for num in factors_a:
            if num in factors_b:
                common_factors.append(num)
        return max(common_factors)

    return find_gcf(numbers[46], numbers[13])
