
def gcf_three_nums(lst):
    def find_gcf(a, b):
        while b:
            a, b = b, a % b
        return a

    index1, index2, index3 = 477, 696, 663
    num1, num2, num3 = lst[index1], lst[index2], lst[index3]
    
    return find_gcf(find_gcf(num1, num2), num3)
