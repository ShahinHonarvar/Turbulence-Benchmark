
from collections import deque

def lists_with_product_equal_n(circle):
    circle = deque(circle)
    result = []
    length = len(circle)
    
    for i in range(length):
        current_product = 1
        for j in range(i, length):
            current_product *= circle[j]
            if current_product == -115:
                result.append(list(circle[i:j+1]))
            elif abs(current_product) > abs(-115):
                break
        circle.rotate(-1)
    return result
