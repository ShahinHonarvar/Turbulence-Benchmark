
def gcf_two_nums(num_list):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    return gcd(num_list[20], num_list[83])
