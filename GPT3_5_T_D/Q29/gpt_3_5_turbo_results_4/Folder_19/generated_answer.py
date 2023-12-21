
def gcf_two_nums(lst):
    a = lst[66]
    b = lst[90]
    
    while b != 0:
        a, b = b, a % b
    
    return a
