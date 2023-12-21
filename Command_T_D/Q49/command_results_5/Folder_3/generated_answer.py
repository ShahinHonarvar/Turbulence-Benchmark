import re
def if_decimal_is_divisible(s):
    i = re.findall(r'(0b)(?P<val>[01]+)', s)
    return (10**len(i[0])-2)//(2**len(i[0])-1)%(10**(len(i[0])-1))==35
