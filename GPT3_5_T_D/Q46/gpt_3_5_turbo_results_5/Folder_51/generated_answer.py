
def gcf_three_nums(num_list):
    num1 = num_list[21]
    num2 = num_list[69]
    num3 = num_list[41]
    
    def find_gcd(x, y):
        while(y):
            x, y = y, x % y
        return x
    
    gcd = find_gcd(num1, find_gcd(num2, num3))
    return gcd
