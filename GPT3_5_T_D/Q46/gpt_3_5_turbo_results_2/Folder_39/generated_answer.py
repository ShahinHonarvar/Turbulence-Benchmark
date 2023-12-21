
def gcf_three_nums(lst):
    def find_factors(n):
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        return factors

    def find_gcf(a, b):
        a_factors = find_factors(a)
        b_factors = find_factors(b)
        gcf = 1
        for factor in a_factors:
            if factor in b_factors:
                gcf = factor
        return gcf

    return find_gcf(lst[85], lst[36], lst[54])
