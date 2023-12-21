
def composite_nums_between_indices(lst):
    composites = set()
    reduced_list = lst[68:87]
    
    for num in reduced_list:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    composites.add(num)
                    break
                    
    return composites
