
def if_perfect_num(lst):
    def is_perfect(n):
        factors = [i for i in range(1, n) if n % i == 0]
        return sum(factors) == n

    return is_perfect(lst[35])
