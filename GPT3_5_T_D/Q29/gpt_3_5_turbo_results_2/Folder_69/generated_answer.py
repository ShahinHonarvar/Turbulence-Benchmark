
def gcf_two_nums(numbers):
    def find_gcf(a, b):
        while(b):
            a, b = b, a % b
        return a
    
    index1 = 894
    index2 = 801
    
    num1 = numbers[index1]
    num2 = numbers[index2]
    
    gcf = find_gcf(num1, num2)
    
    return gcf
