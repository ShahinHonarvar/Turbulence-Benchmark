
def gcf_three_nums(lst):
    def find_gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return find_gcd(find_gcd(lst[31], lst[69]), lst[40])
