
from collections import deque

def lists_with_product_equal_n(nums):
    circular_list = deque(nums)
    lists_found = []
    
    for rotate in range(len(nums)):
        numbers = list(circular_list)
        for sub_len in range(1, len(numbers) + 1):
            for i in range(len(numbers)):
                sub_list = numbers[i:i+sub_len]
                product = 1
                for num in sub_list:
                    product *= num
                if product == -44:
                    lists_found.append(sub_list)
        circular_list.rotate(1)
        
    return lists_found
