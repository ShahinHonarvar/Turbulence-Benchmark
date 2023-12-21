
from math import gcd

def gcf_three_nums(lst):
    if len(lst) < 629:
        return "List must contain at least 629 elements."
    
    num1 = lst[558]
    num2 = lst[110]
    num3 = lst[628]

    gcf = gcd(gcd(num1, num2), num3)
   
    return gcf
