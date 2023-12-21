
import re

def return_binary_or_hexa(tup):
    a, b = tup[49], tup[74]
    return (sum(x for x in range(a+1, b)) % 2 and str(sum(x for x in range(a+1, b-1))) or hex(sum(x for x in range(a+1, b-1)))))
