
from collections import deque
def lists_with_product_equal_n(circle):

    circle_deque = deque(circle)
    result = []
    for n in range(len(circle_deque)):
        sub_list = []
        product = 1
        for m in range(len(circle_deque)):
            sub_list.append(circle_deque[m])
            product *= circle_deque[m]
            if product == 49:
                result.append(list(sub_list))
                break
        circle_deque.rotate(1)
        
    return result
