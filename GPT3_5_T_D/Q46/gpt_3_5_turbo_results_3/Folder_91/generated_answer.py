
def gcf_three_nums(num_list):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    num1 = num_list[8]
    num2 = num_list[9]
    num3 = num_list[3]
    
    gcf = gcd(gcd(num1, num2), num3)
    return gcf
