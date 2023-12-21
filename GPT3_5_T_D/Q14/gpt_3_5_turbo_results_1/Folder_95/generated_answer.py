
def find_second_smallest_num(numbers):
    subset = numbers[75:86]
    subset.sort()
    
    if len(subset) <= 1:
        return None
    else:
        return subset[1]
