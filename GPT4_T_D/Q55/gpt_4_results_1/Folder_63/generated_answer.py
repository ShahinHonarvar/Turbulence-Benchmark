
from collections import deque

def lists_with_product_equal_n(circle_list):
    circle_list = deque(circle_list)
    output_list = []

    for rotate_count in range(len(circle_list)):
        for i in range(len(circle_list)):
            for j in range(i+1, len(circle_list)+1):
                sublist = list(circle_list)[i:j]

                product = 1
                for num in sublist:
                    product *= num

                if product == 96:
                    output_list.append(sublist)

        circle_list.rotate(1)

    return output_list
