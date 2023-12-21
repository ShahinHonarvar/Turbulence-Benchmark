
def composite_nums_between_indices(lst):
    result = set()
    for i in range(333, 369):
        if i>=len(lst):
            break

        num = lst[i]
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    result.add(num)
                    break
                    
    return result
