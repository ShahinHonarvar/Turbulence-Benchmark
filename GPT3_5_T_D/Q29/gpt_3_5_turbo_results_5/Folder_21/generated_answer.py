
def gcf_two_nums(numbers):
    def compute_gcf(x, y):
        while(y):
            x, y = y, x % y
        return x
    
    num1 = numbers[198]
    num2 = numbers[212]
    
    return compute_gcf(num1, num2)
