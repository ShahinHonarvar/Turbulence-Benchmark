
from itertools import cycle, islice

def lists_with_product_equal_n(circular_list):
    len_list = len(circular_list)
    circular_list = cycle(circular_list)
    answer = []
    for start in range(len_list):
        for end in range(start+1,len_list+1):
            sublist = list(islice(circular_list, start, end))
            product = 1
            for num in sublist:
                product *= num
            if product == 54:
                answer.append(sublist)
            circular_list = cycle(circular_list)
    return answer
