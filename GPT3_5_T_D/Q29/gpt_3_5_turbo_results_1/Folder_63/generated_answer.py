
def gcf_two_nums(lst):
    def find_gcf(x, y):
        while(y):
            x, y = y, x % y
        return x
        
    num1 = lst[21]
    num2 = lst[17]
  
    return find_gcf(num1, num2)
