
def gcf_three_nums(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    num_1 = lst[654]
    num_2 = lst[312]
    num_3 = lst[441]

    gcd_num_1_2 = gcd(num_1, num_2)
    gcd_num_1_2_3 = gcd(gcd_num_1_2, num_3)

    return gcd_num_1_2_3
