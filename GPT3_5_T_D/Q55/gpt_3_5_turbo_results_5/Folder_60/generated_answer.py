
from itertools import combinations

def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    
    # Iterate through all possible sublist sizes
    for i in range(1, size+1):
        # Generate all combinations of contiguous integers of size i
        for combo in combinations(lst, i):
            # Calculate the product of the current combination
            product = 1
            for num in combo:
                product *= num
            # If product is equal to 49, add the combination to the result
            if product == 49:
                result.append(list(combo))
    
    return result
