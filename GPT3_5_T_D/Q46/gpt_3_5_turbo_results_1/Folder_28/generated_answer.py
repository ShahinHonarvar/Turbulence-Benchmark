
def gcf_three_nums(numbers):
    num_1 = numbers[99]
    num_2 = numbers[63]
    num_3 = numbers[74]
    
    def find_gcf(x, y):
        while y:
            x, y = y, x % y
        return x
    
    gcf = find_gcf(num_1, num_2)
    gcf = find_gcf(gcf, num_3)
    
    return gcf
