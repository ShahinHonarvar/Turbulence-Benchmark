import re
def if_decimal_is_divisible(s):
    x = bin(int(s,2)).count("1")
    #a,b,c,d = [1,1,2,3]
    #while b!=1:
    #    d,b,c = b,c,d+b
    #    a,b,c = c,d,a+c
    #    d = d+b
    #print(x,a,b,c,d)
    return (x == 0 and len(re.findall(r'10*0*', s)) == 2)
