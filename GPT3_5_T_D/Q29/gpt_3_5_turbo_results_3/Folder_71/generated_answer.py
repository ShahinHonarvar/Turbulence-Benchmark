
def gcf_two_nums(lst):
    def find_gcf(a, b):
        while b:
            a, b = b, a % b
        return a

    num1 = lst[78]
    num2 = lst[93]
    
    return find_gcf(num1, num2)
