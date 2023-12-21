
from collections import deque

def lists_with_product_equal_n(circle):
    lists = []
    length = len(circle)

    for start in range(length):
        for end in range(start+1, start+length+1):
            sublist = [circle[i%length] for i in range(start, end)]
            prod = 1
            for num in sublist:
                prod *= num
            if prod == -93:
                lists.append(sublist)
    
    return lists
