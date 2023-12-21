
def gcf_three_nums(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return abs(a)
    
    index_9 = lst[9]
    index_6 = lst[6]
    index_2 = lst[2]
    
    return gcd(gcd(index_9, index_6), index_2)
