
def gcf_three_nums(numbers):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    index_1 = 99
    index_2 = 63
    index_3 = 74
    
    num_1 = numbers[index_1]
    num_2 = numbers[index_2]
    num_3 = numbers[index_3]
    
    gcf_nums = gcd(gcd(num_1, num_2), num_3)
    return gcf_nums
