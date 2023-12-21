
def lists_with_product_equal_n(c_list):
    from operator import mul
    from functools import reduce
    from itertools import combinations
    result_list = []
    n = -10
    # Adjusting for circularity by appending list elements to length of list to create potential wrap-around combinations.
    c_list = c_list + c_list[:len(c_list)-1]
    for i in range(1, len(c_list)):
      # Use 'combinations' from itertools to generate contiguous sublists
      # 'combinations' function actually gives combinations, but as we're giving it a range starting from 1 every time, 
      # we get different size contiguous sublists
        for combination in combinations(c_list, i):
            if abs(reduce(mul, combination, 1)) == abs(n):
                result_list.append(list(combination))
    return result_list
