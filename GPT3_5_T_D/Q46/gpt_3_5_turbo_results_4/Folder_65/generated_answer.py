
def gcf_three_nums(numbers):
    def find_gcf(x, y):
        while(y):
            x, y = y, x % y
        return x
    
    num_1 = numbers[18]
    num_2 = numbers[10]
    num_3 = numbers[76]
    
    gcf = find_gcf(num_1, num_2)
    gcf = find_gcf(gcf, num_3)
    
    return gcf
