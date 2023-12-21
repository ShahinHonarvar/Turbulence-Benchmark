
def gcf_two_nums(num_lst):
    def gcd(x, y):
        while(y):
            x, y = y, x % y
        return x
    return gcd(num_lst[86], num_lst[89])
