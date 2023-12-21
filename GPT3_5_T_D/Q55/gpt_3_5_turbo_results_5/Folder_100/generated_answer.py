
from itertools import combinations

def lists_with_product_equal_n(numbers):
    sublists = []
    n = len(numbers)
    for size in range(1, n+1):
        for i in range(n):
            sublist = numbers[i:i+size] + numbers[:size-(n-i)]
            product = 1
            for num in sublist:
                product *= num
            if product == 48:
                sublists.append(sublist)
    return sublists
