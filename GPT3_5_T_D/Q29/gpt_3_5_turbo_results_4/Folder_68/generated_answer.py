
def gcf_two_nums(num_list):
    def find_gcd(x, y):
        while (y):
            x, y = y, x % y
        return x

    if len(num_list) >= 10:
        a = num_list[8]
        b = num_list[9]
        gcd = find_gcd(a, b)
        return gcd
    else:
        return None
