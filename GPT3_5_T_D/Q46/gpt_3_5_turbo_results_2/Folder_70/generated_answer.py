
def gcf_three_nums(numbers):
    a = numbers[990]
    b = numbers[671]
    c = numbers[711]
    
    def gcf(a, b):
        while(b):
            a, b = b, a % b
        return a
    
    gcf_ab = gcf(a, b)
    gcf_abc = gcf(gcf_ab, c)
    return gcf_abc
